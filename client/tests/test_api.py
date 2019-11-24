from django.urls import reverse


def test_create_client_success(client, db, mock_client):
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


def test_get_client_success(client, db, mock_token):
    """Test"""
    url = reverse("client:crud")
    response = client.get(url,
                          content_type='application/json',
                          **mock_token)
    data = response.json()
    assert response.status_code == 200
    assert data
    assert data["id"]
    assert data["name"]
    assert data["email"]


def test_update_client_not_authorized(client, db):
    """Test"""
    url = reverse("client:crud")
    mock_client = {"name": "update_client"}
    mock_token = {'HTTP_AUTHORIZATION': '123'}
    response = client.put(url, data=mock_client,
                          content_type='application/json',
                          **mock_token)
    assert response.status_code == 401


def test_update_client_success(client, db, mock_token):
    """Test"""
    url = reverse("client:crud")
    mock_client = {"name": "update_client"}
    response = client.put(url, data=mock_client,
                          content_type='application/json',
                          **mock_token)
    assert response.status_code == 200
    assert response.json()["name"] == mock_client["name"]


def test_update_client_error(client, db, mock_token):
    """Test"""
    url = reverse("client:crud")
    mock_client = {"name": ""}
    response = client.put(url, content_type='application/json',
                          data=mock_client, **mock_token)
    assert response.status_code == 400


def test_patch_client_success(client, db, mock_token):
    """Test"""
    url = reverse("client:crud")
    mock_client = {"name": "update_client"}
    response = client.patch(url, data=mock_client,
                            content_type='application/json',
                            **mock_token)
    assert response.status_code == 200
    assert response.json()["name"] == mock_client["name"]


def test_patch_client_error(client, db, mock_token):
    """Test"""
    url = reverse("client:crud")
    mock_client = {"name": ""}
    response = client.patch(url, content_type='application/json',
                            data=mock_client, **mock_token)
    assert response.status_code == 400
