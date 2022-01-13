from app import app
import pytest
"""
@pytest.fixture
def client():
    _app = app
    yield client
"""
@pytest.fixture
def client():
    with app.app_context():
        with app.test_client() as client:
            yield client