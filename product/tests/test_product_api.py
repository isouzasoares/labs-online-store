from django.urls import reverse

from model_bakery import baker
from product.models import Product
from product.serializers import ProductSerializer


def test_product_list_success(db, client):
    """Test"""
    url = reverse("product:list")
    product = baker.make(Product)
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert [ProductSerializer(product).data] == data["results"]
    assert not data["next"]


def test_product_list_not_items(db, client):
    """Test"""
    url = reverse("product:list")
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 0
    assert not data["next"]


def test_product_list_some_items(db, client):
    """Test"""
    url = reverse("product:list")
    for item in range(200):
        baker.make(Product)
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 200
    assert data["next"]


def test_product_list_with_pagination(db, client):
    """Test"""
    url = reverse("product:list")
    for item in range(200):
        baker.make(Product)
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 200
    response = client.get(data["next"])
    assert response.status_code == 200
    response = client.get(response.json()["previous"])
    assert response.status_code == 200
    response = client.get(response.json()["previous"])
    assert response.status_code == 404


def test_product_get(db, client):
    """Test"""
    product = baker.make(Product)
    url = reverse("product:get", args=(product.pk,))
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert ProductSerializer(product).data == data


def test_product_get_error(db, client):
    """Test"""
    url = reverse("product:get", args=(2,))
    response = client.get(url)
    assert response.status_code == 404
