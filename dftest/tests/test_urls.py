import pytest
from django.urls import reverse, resolve
from django.test import Client
from django.contrib.admin.sites import AdminSite

def test_admin_url():
    """Test that admin URL resolves correctly"""
    url = reverse('admin:index')
    assert url == '/admin/'
    resolver = resolve(url)
    assert resolver.app_name == 'admin'

def test_index_url():
    """Test that index URL resolves correctly"""
    url = reverse('index')
    assert url == '/'
    resolver = resolve(url)
    assert resolver.func.__name__ == 'index'

def test_index_view(client):
    """Test that index view returns 200 and uses correct template"""
    response = client.get('/')
    assert response.status_code == 200
    assert 'django_deepface/index.html' in [t.name for t in response.templates]

def test_deepface_urls_included():
    """Test that django_deepface URLs are included"""
    from django.urls import get_resolver
    resolver = get_resolver()
    # Check that django_deepface URLs are in the resolver
    assert any('django_deepface' in str(pattern) for pattern in resolver.url_patterns) 