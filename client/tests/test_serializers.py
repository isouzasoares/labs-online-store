import pytest
from model_bakery import baker
from client.serializers import ClientCreateSerializer
from client.models import Client


def test_client_create_serializer_success(db, mock_client):
    """Test"""
    serializer = ClientCreateSerializer(data=mock_client)
    assert serializer.is_valid()


@pytest.mark.parametrize("data_pop", ["email", "name", "password"])
def test_client_create_with_not_data(db, data_pop, mock_client):
    """Test"""
    mock_client.pop(data_pop)
    serializer = ClientCreateSerializer(data=mock_client)
    assert not serializer.is_valid()
    assert data_pop in serializer.errors


def test_client_create_with_invalid_email(db, mock_client):
    """Test"""
    mock_client["email"] = "test"
    serializer = ClientCreateSerializer(data=mock_client)
    assert not serializer.is_valid()
    assert "email" in serializer.errors


def test_client_is_unique(db, mock_client):
    """Test"""
    mock_model = baker.make(Client)
    mock_client["email"] = mock_model.email
    serializer = ClientCreateSerializer(data=mock_client)
    assert not serializer.is_valid()
    assert "There is already an account with this email" \
           in str(serializer.errors["email"][0])
