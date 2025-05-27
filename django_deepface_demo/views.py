"""Views for django_deepface_demo app."""

from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from .models import CaptureDevice


def index(request):
    """Home page view."""
    return render(request, "django_deepface_demo/index.html")


@staff_member_required
def device_stats_view(request):
    """View for displaying device statistics."""
    # Get browser statistics
    browser_stats = (
        CaptureDevice.objects.values("browser")
        .annotate(count=Count("id"))
        .order_by("-count")
    )

    # Get OS statistics
    os_stats = (
        CaptureDevice.objects.values("os")
        .annotate(count=Count("id"))
        .order_by("-count")
    )

    # Get device type statistics
    device_stats = (
        CaptureDevice.objects.values("device_type")
        .annotate(count=Count("id"))
        .order_by("-count")
    )

    context = {
        "browser_stats": list(browser_stats),
        "os_stats": list(os_stats),
        "device_stats": list(device_stats),
    }
    return render(request, "django_deepface_demo/device_stats.html", context)
