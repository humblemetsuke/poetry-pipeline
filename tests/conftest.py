# conftest.py
import coverage

# import pytest


def pytest_sessionfinish(session, exitstatus):
    """
    This hook runs after all tests finish.
    Generates an HTML coverage report automatically.
    """

    # points to default coverage file
    cov = coverage.Coverage(data_file=".coverage")
    cov.load()
    cov.html_report(directory="htmlcov")  # generates htmlcov/index.html
    print("\nHTML coverage report generated at htmlcov/index.html")
