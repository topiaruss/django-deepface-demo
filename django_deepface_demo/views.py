"""Views for django_deepface_demo app."""

from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.contrib import messages
from django.urls import reverse
from .models import CaptureDevice
from .forms import QuickRegistrationForm


def index(request):
    """Home page view."""
    return render(request, "django_deepface_demo/index.html")


def quick_register(request):
    """Quick registration view that redirects to login with credentials."""
    if request.method == 'POST':
        form = QuickRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Add success message with credentials
            messages.success(
                request,
                f"Registration successful! Your username is '{user.username}' and your password is what you entered."
            )
            return redirect('django_deepface:login')
    else:
        form = QuickRegistrationForm()
    return render(request, "django_deepface_demo/register.html", {"form": form})


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
