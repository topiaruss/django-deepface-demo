"""Test suite for django_deepface_demo."""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_deepface_demo.models import CaptureDevice

User = get_user_model()


class DeepFaceTestSuite(TestCase):
    """Test suite for DeepFace functionality."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
            is_staff=True,  # Make the user a staff member
        )

    def test_device_stats_view(self):
        """Test device stats view."""
        # Create some test device data
        CaptureDevice.objects.create(
            user_agent="Mozilla/5.0",
            browser="Chrome",
            os="MacOS",
            device_type="Desktop",
            engine="Blink",
            was_successful=True,
        )

        # Test the view
        response = self.client.get(reverse("django_deepface_demo:stats"))
        self.assertEqual(response.status_code, 302)  # Redirects to login

        # Login and try again
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("django_deepface_demo:stats"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "django_deepface_demo/device_stats.html")
