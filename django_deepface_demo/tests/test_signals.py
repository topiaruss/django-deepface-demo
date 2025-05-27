from django.test import TestCase, RequestFactory
from django_deepface.signals import face_image_processed
from django_deepface_demo.models import CaptureDevice


class SignalTests(TestCase):
    """Test signal handlers."""

    def setUp(self):
        """Set up test data."""
        self.factory = RequestFactory()
        # Sample user agent string for Chrome on macOS
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

    def test_face_image_processed_signal(self):
        """Test that face_image_processed signal creates a CaptureDevice record."""
        # Create a request with the user agent
        request = self.factory.get("/")
        request.META["HTTP_USER_AGENT"] = self.user_agent

        # Send the signal
        face_image_processed.send(sender=self.__class__, request=request)

        # Verify that a CaptureDevice record was created
        self.assertEqual(CaptureDevice.objects.count(), 1)
        device = CaptureDevice.objects.first()
        # Verify the device information
        self.assertEqual(device.user_agent, self.user_agent)
        self.assertEqual(device.browser, "Chrome")
        self.assertEqual(device.os, "Mac")
        self.assertEqual(device.device_type, "desktop")
        self.assertEqual(
            device.engine, "{'default': 'WebKit', 'versions': {28: 'Blink'}}"
        )
        self.assertTrue(device.was_successful)
