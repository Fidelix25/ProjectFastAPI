import pytest
from fastapi.testclient import TestClient

from projectfastapi.app import app


@pytest.fixture
def client():
    return TestClient(app)
