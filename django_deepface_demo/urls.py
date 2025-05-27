"""URL configuration for django_deepface_demo app."""

from django.urls import path
from . import views

app_name = "django_deepface_demo"

urlpatterns = [
    path("", views.index, name="index"),
    path("device-stats/", views.device_stats_view, name="device_stats"),
]
