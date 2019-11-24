import pytest


@pytest.fixture
def mock_product():
    """Dict with product mock"""
    return {
        "title": "Chrome cast",
        "brand": "google",
        "price": "45.00",
        "image": "http://www.google.com",
        "reviewScore": 1.0,
    }
