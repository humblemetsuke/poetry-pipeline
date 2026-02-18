import pytest
from fastapi.testclient import TestClient

from app.main import app, delay_function

client = TestClient(app)

"""
Below are happy path unit tests. They check the endpoint
and determine if it behaves as expected. It also verifies json file structure
is valid.
"""


# -----------------------------
# Test the root endpoint
# -----------------------------
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    json_data = response.json()
    assert "message" in json_data
    assert "hostname" in json_data
    assert "environment" in json_data


def test_root_response_schema():
    response = client.get("/")
    data = response.json()
    assert isinstance(data.get("message"), str)
    assert isinstance(data.get("hostname"), str)
    assert isinstance(data.get("environment"), str)


# --------------------------------
# Test the health endpoint
# ------------------------------


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data == {"status": "ok"}


# ----------------
# Edge case tests
# ----------------


def test_non_existent_path():
    response = client.get("/non-existent")
    # FastAPI returns 404 for unknown paths
    assert response.status_code == 404


def test_malformed_url():
    # URLs with illegal characters: usually rejected by the client
    with pytest.raises(Exception):
        client.get("/this is invalid")


def test_empty_path():
    # '' is equivalent to root
    response = client.get("")
    assert response.status_code == 200  # Success code
    assert "message" in response.json()


def test_wrong_http_method():
    # POST request to GET-only endpoint should fail
    response = client.post("/")
    assert response.status_code == 405  # Method Not Allowed
    response = client.post("/health")
    assert response.status_code == 405


def test_query_parameter_ignored():
    # Even if user sends random query params, endpoint should ignore them
    response = client.get("/?foo=bar&baz=123")
    assert response.status_code == 200
    json_data = response.json()
    assert "message" in json_data


# -----------------------------
# Invalid input type tests
# -----------------------------


def test_root_with_invalid_query_param_type():

    response = client.get("/?foo[]=bar&foo[]=baz")
    assert response.status_code == 200  # endpoint ignores unknown params
    json_data = response.json()
    assert "message" in json_data


def test_wrong_type_post_to_root():
    # If you add POST to a GET-only endpoint with invalid data
    response = client.post("/", json={"message": 123})
    assert response.status_code == 405  # Method Not Allowed


# -----------------------------
# Invalid input type tests for health endpoint
# -----------------------------
def test_health_with_unexpected_body():
    # Health endpoint is GET and expects no body, send JSON anyway
    response = client.get("/health", json={"unexpected": "data"})
    assert response.status_code == 200  # FastAPI ignores GET bodies
    json_data = response.json()
    assert json_data == {"status": "ok"}


# --------------------------------------------
# Test slow endpoint to measure delay response
# --------------------------------------------


def fake_delay():
    pass  # No delay, instant return


app.dependency_overrides[delay_function] = fake_delay


def test_slow_endpoint():
    response = client.get("/slow")
    assert response.status_code == 200
    assert response.json() == {"status": "slow response"}
