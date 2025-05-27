from django.db import models

class CaptureDevice(models.Model):
    user_agent = models.TextField()
    browser = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50)
    engine = models.CharField(max_length=50)
    was_successful = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'django_deepface_demo'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.browser} on {self.os} ({self.device_type}) - {'Success' if self.was_successful else 'Failed'}" 