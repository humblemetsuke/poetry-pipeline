import httpx
import pytest
from fastapi.testclient import TestClient

from app.main import app, delay_function


# -----------------------------
# Fixtures
# -----------------------------
@pytest.fixture
def client():
    return TestClient(app)


# -----------------------------
# Happy path tests
# -----------------------------
def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    json_data = response.json()
    assert "message" in json_data
    assert "hostname" in json_data
    assert "environment" in json_data


def test_root_response_schema(client):
    data = client.get("/").json()
    assert isinstance(data.get("message"), str)
    assert isinstance(data.get("hostname"), str)
    assert isinstance(data.get("environment"), str)


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# -----------------------------
# Edge case / error tests
# -----------------------------
def test_non_existent_path(client):
    response = client.get("/non-existent")
    assert response.status_code == 404


def test_malformed_url(client):
    # URLs with illegal characters: should raise a RequestError
    with pytest.raises(httpx.InvalidURL):
        client.get("http://:::invalid-url")


def test_empty_path(client):
    response = client.get("")
    assert response.status_code == 200
    assert "message" in response.json()


def test_wrong_http_method(client):
    response = client.post("/")
    assert response.status_code == 405  # Method Not Allowed
    response = client.post("/health")
    assert response.status_code == 405


def test_query_parameter_ignored(client):
    response = client.get("/?foo=bar&baz=123")
    assert response.status_code == 200
    assert "message" in response.json()


# -----------------------------
# Invalid input type tests
# -----------------------------
def test_root_with_invalid_query_param_type(client):
    response = client.get("/?foo[]=bar&foo[]=baz")
    assert response.status_code == 200
    assert "message" in response.json()


def test_wrong_type_post_to_root(client):
    response = client.post("/", json={"message": 123})
    assert response.status_code == 405  # Method Not Allowed


def test_health_with_unexpected_body(client):
    # Use client.request directly for GET with body
    response = client.request("GET", "/health", data=b'{"unexpected":"data"}')
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# -----------------------------
# Slow endpoint test
# -----------------------------
def fake_delay():
    return  # No delay for testing


app.dependency_overrides[delay_function] = fake_delay


def test_slow_endpoint(client):
    response = client.get("/slow")
    assert response.status_code == 200
    assert response.json() == {"status": "slow response"}
