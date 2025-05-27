from django.dispatch import receiver
from django_deepface.signals import face_image_processed
from device_detector import DeviceDetector
from .models import CaptureDevice


@receiver(face_image_processed)
def handle_face_image_processed(sender, request, **kwargs):
    """Handle successful face image processing by creating a CaptureDevice record."""
    user_agent = request.META.get("HTTP_USER_AGENT", "")
    dd = DeviceDetector(user_agent)
    dd.parse()
    CaptureDevice.objects.create(
        user_agent=user_agent,
        browser=dd.client_name() or "",
        browser_version=dd.client_version() or "",
        os=dd.os_name() or "",
        os_version=dd.os_version() or "",
        device_type=dd.device_type() or "",
        device_brand=dd.device_brand() or "",
        device_model=dd.device_model() or "",
        engine=dd.engine() or "",
        stage=kwargs.get("stage", ""),
        was_successful=True,
    )
