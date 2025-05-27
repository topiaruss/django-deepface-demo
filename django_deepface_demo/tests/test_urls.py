"""Test URL patterns for django_deepface_demo."""
from django.test import TestCase
from django.urls import reverse, resolve

class URLTests(TestCase):
    """Test URL patterns."""

    def test_device_stats_url(self):
        """Test device stats URL."""
        url = reverse("django_deepface_demo:device_stats")
        self.assertEqual(url, "/demo/device-stats/")
        self.assertEqual(resolve(url).func.__name__, "device_stats_view")

    def test_index_url(self):
        """Test index URL."""
        url = reverse("django_deepface_demo:index")
        self.assertEqual(url, "/demo/")
        self.assertEqual(resolve(url).func.__name__, "index") 