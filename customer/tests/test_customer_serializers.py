import pytest
from model_bakery import baker
from customer.serializers import CustomerCreateSerializer
from customer.models import Customer


def test_client_create_serializer_success(db, mock_customer):
    """Test"""
    serializer = CustomerCreateSerializer(data=mock_customer)
    assert serializer.is_valid()


@pytest.mark.parametrize("data_pop", ["email", "name", "password"])
def test_client_create_with_not_data(db, data_pop, mock_customer):
    """Test"""
    mock_customer.pop(data_pop)
    serializer = CustomerCreateSerializer(data=mock_customer)
    assert not serializer.is_valid()
    assert data_pop in serializer.errors


def test_client_create_with_invalid_email(db, mock_customer):
    """Test"""
    mock_customer["email"] = "test"
    serializer = CustomerCreateSerializer(data=mock_customer)
    assert not serializer.is_valid()
    assert "email" in serializer.errors


def test_client_is_unique(db, mock_customer):
    """Test"""
    mock_model = baker.make(Customer)
    mock_customer["email"] = mock_model.email
    serializer = CustomerCreateSerializer(data=mock_customer)
    assert not serializer.is_valid()
    assert "There is already an account with this email" in str(
        serializer.errors["email"][0]
    )
