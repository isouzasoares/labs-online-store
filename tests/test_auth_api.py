import pytest
from django.urls import reverse


def test_get_token(client, django_user_model):
    data = {"email": "user1@user.com", "password": "bar"}
    django_user_model.objects.create_user(username="user1", **data)
    url = reverse("token_obtain_pair")
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert response.json()["access"]
    assert response.json()["refresh"]


def test_refresh_token(client, django_user_model):
    data = {"email": "user1@user.com", "password": "bar"}
    django_user_model.objects.create_user(username="user1", **data)
    url = reverse("token_obtain_pair")
    response = client.post(url, data=data)
    response = response.json()
    response = client.post(
        reverse("token_refresh"), data={"refresh": response["refresh"]}
    )
    assert response.status_code == 200


def test_get_token_unauthorized(db, client):
    data = {"email": "user1@user.com", "password": "bar"}
    response = client.post(reverse("token_obtain_pair"), data=data)
    assert response.status_code == 401


@pytest.mark.parametrize("swagger_endswith", [".yaml", ".json", "/"])
def test_swagger(client, swagger_endswith):
    """Test"""
    response = client.get(f"/api/swagger{swagger_endswith}")
    assert response.status_code == 200
