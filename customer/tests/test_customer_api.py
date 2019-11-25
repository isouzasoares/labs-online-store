from django.urls import reverse


def test_create_customer_success(client, db, mock_customer):
    """Test"""
    url = reverse("customer:create")
    response = client.post(url, data=mock_customer)
    assert response.status_code == 201


def test_create_customer_error(client, db, mock_customer):
    """Test"""
    url = reverse("customer:create")
    mock_customer.pop("email")
    response = client.post(url, data=mock_customer)
    assert response.status_code == 400


def test_get_customer_success(client, db, mock_token):
    """Test"""
    url = reverse("customer:crud")
    response = client.get(url, content_type="application/json", **mock_token)
    data = response.json()
    assert response.status_code == 200
    assert data
    assert data["id"]
    assert data["name"]
    assert data["email"]


def test_update_customer_not_authorized(client, db):
    """Test"""
    url = reverse("customer:crud")
    mock_customer = {"name": "update_client"}
    mock_token = {"HTTP_AUTHORIZATION": "123"}
    response = client.put(
        url, data=mock_customer, content_type="application/json", **mock_token
    )
    assert response.status_code == 401


def test_update_customer_success(client, db, mock_token):
    """Test"""
    url = reverse("customer:crud")
    mock_customer = {"name": "update_client"}
    response = client.put(
        url, data=mock_customer, content_type="application/json", **mock_token
    )
    assert response.status_code == 200
    assert response.json()["name"] == mock_customer["name"]


def test_update_customer_error(client, db, mock_token):
    """Test"""
    url = reverse("customer:crud")
    mock_customer = {"name": ""}
    response = client.put(
        url, content_type="application/json", data=mock_customer, **mock_token
    )
    assert response.status_code == 400


def test_patch_customer_success(client, db, mock_token):
    """Test"""
    url = reverse("customer:crud")
    mock_customer = {"name": "update_client"}
    response = client.patch(
        url, data=mock_customer, content_type="application/json", **mock_token
    )
    assert response.status_code == 200
    assert response.json()["name"] == mock_customer["name"]


def test_patch_customer_error(client, db, mock_token):
    """Test"""
    url = reverse("customer:crud")
    mock_customer = {"name": ""}
    response = client.patch(
        url, content_type="application/json", data=mock_customer, **mock_token
    )
    assert response.status_code == 400


def test_delete_not_authorized(client, db, mock_token):
    """Test"""
    url = reverse("customer:crud")
    mock_token = {"HTTP_AUTHORIZATION": "123"}
    response = client.delete(
        url, content_type="application/json", **mock_token
    )
    assert response.status_code == 401


def test_delete_success(client, db, mock_token):
    """Test"""
    url = reverse("customer:crud")
    response = client.delete(
        url, content_type="application/json", **mock_token
    )
    assert response.status_code == 204


def test_delete_and_access_item(client, db, mock_token):
    """Test"""
    url = reverse("customer:crud")
    delete_resp = client.delete(
        url, content_type="application/json", **mock_token
    )
    response = client.get(url, content_type="application/json", **mock_token)
    assert delete_resp.status_code == 204
    assert response.status_code == 401


def test_create_product_favorite_success(client, db, mock_token,
                                         mock_favorite):
    """Test"""
    url = reverse("customer:favorite_product")
    response = client.post(
        url, data=mock_favorite, content_type="application/json",
        **mock_token
    )
    assert response.status_code == 201


def test_create_product_favorite_remove_success(client, db, mock_token,
                                                mock_favorite):
    """Test"""
    url = reverse("customer:favorite_product")
    response = client.post(
        url, data=mock_favorite, content_type="application/json",
        **mock_token
    )
    delete_resp = client.post(
        url, data=mock_favorite, content_type="application/json",
        **mock_token
    )
    assert response.status_code == 201
    assert delete_resp.status_code == 204


def test_product_favorite_list_success(client, db, mock_token,
                                       mock_favorite):
    """Test"""
    url = reverse("customer:favorite_product")
    client.post(
        url, data=mock_favorite, content_type="application/json",
        **mock_token
    )
    response = client.get(
        url, content_type="application/json",
        **mock_token
    )
    delete_resp = client.post(
        url, data=mock_favorite, content_type="application/json",
        **mock_token
    )
    response_deleted = client.get(
        url, content_type="application/json",
        **mock_token
    )
    assert response.status_code == 200
    assert response.json()["count"] == 1
    assert delete_resp.status_code == 204
    assert response_deleted.json()["count"] == 0


def test_product_favorite_list_create_not_login(client, db, mock_token,
                                                mock_favorite):
    """Test"""
    url = reverse("customer:favorite_product")
    post_response = client.post(
        url, data=mock_favorite, content_type="application/json",
    )
    get_response = client.get(
        url, content_type="application/json",
    )
    assert post_response.status_code == 401
    assert get_response.status_code == 401
