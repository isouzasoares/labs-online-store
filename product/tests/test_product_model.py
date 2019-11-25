from model_bakery import baker
from product.models import Product


def test_product_model_str(db):
    """Test"""
    product = baker.make(Product)
    assert str(product) == product.title
