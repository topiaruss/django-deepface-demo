from django.contrib import admin
from .models import CaptureDevice


@admin.register(CaptureDevice)
class CaptureDeviceAdmin(admin.ModelAdmin):
    list_display = (
        "stage",
        "browser",
        "os",
        "device_type",
        "engine",
        "was_successful",
        "created_at",
    )
    search_fields = ("browser", "os", "device_type", "engine")
    list_filter = ("stage", "browser", "os", "device_type", "engine", "was_successful")
