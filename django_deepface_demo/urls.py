"""URL configuration for django_deepface_demo app."""

from django.urls import path
from . import views

app_name = "django_deepface_demo"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.quick_register, name="register"),
    path("stats/", views.device_stats_view, name="stats"),
]
