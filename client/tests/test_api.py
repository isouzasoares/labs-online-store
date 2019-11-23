import pytest
from django.urls import reverse


def test_create_client_sucess(client, db, mock_client):
    """Test"""
    url = reverse("client:create")
    response = client.post(url, data=mock_client)
    assert response.status_code == 201


def test_create_client_error(client, db, mock_client):
    """Test"""
    url = reverse("client:create")
    mock_client.pop("email")
    response = client.post(url, data=mock_client)
    assert response.status_code == 400
