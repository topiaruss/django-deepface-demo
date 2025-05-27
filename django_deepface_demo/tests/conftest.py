"""Pytest configuration for django_deepface_demo tests."""

import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def test_user():
    """Create a test user."""
    return User.objects.create_user(username="testuser", password="testpass123")


@pytest.fixture
def authenticated_client(client, test_user):
    """Create an authenticated client."""
    client.login(username="testuser", password="testpass123")
    return client
