import pytest


@pytest.fixture
def mock_client():
    """Dict with client mock"""
    return {"email": "test@test.com",
            "name": "test",
            "password": "123abc"}
