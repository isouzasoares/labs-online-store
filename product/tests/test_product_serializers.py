import pytest
from product.serializers import ProductSerializer


def test_product_serializer_success(db, mock_product):
    """Test"""
    serializer = ProductSerializer(data=mock_product)
    assert serializer.is_valid()


@pytest.mark.parametrize(
    "item,data_error",
    [("brand", None), ("title", None), ("price", "1a"), ("image", "1a13")],
)
def test_product_serializer_error(item, data_error, db, mock_product):
    """Test"""
    mock_product[item] = data_error
    serializer = ProductSerializer(data=mock_product)
    assert not serializer.is_valid()
