import pytest
from fastapi.testclient import TestClient

from gcp_fastapi_poetry.api import app


@pytest.fixture
def api_client() -> TestClient:
    """
    Return an API test client that can interact with a temporary database
    """
    return TestClient(app)
