""" Adding the fixtures for pytest """

import pytest
from fastapi.testclient import TestClient

from app.core.main import app


@pytest.fixture(scope="module")
def test_app():
    """ Create and yield a client for testing """
    yield TestClient(app)
