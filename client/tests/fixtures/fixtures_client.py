import pytest
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


@pytest.fixture
def mock_client():
    """Dict with client mock"""
    return {"email": "test@test.com",
            "name": "test",
            "password": "123abc"}


@pytest.fixture
def mock_token(django_user_model):
    """Mock token"""
    data = {"name": "icaro",
            "email": "test@test.com",
            "password": "123abc"}
    django_user_model.objects.create_user(username="user1", **data)
    data = {"email": data["email"], "password": data["password"]}
    token = TokenObtainPairSerializer(data=data)
    if token.is_valid():
        headers = {
            'HTTP_AUTHORIZATION': f'Bearer {token.validated_data["access"]}'
        }
        return headers
    return {}
