import pytest
from model_bakery import baker
from product.models import Product


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


@pytest.fixture
def mock_product_model():
    """Mock product object"""
    return baker.make(Product)
