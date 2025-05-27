from django.db import models


class CaptureDevice(models.Model):
    user_agent = models.TextField()
    browser = models.CharField(max_length=100)
    browser_version = models.CharField(max_length=50, null=True, blank=True)
    os = models.CharField(max_length=100)
    os_version = models.CharField(max_length=50, null=True, blank=True)
    device_type = models.CharField(max_length=50)
    device_brand = models.CharField(max_length=50, null=True, blank=True)
    device_model = models.CharField(max_length=100, null=True, blank=True)
    engine = models.CharField(max_length=100, null=True, blank=True)
    stage = models.CharField(max_length=20, null=True, blank=True)
    was_successful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "django_deepface_demo"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.browser} on {self.os} ({self.device_type}) - {'Success' if self.was_successful else 'Failed'}"
