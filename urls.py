from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", RedirectView.as_view(url="/demo/", permanent=True)
    ),  # Redirect root to demo
    path(
        "demo/", include("django_deepface_demo.urls", namespace="django_deepface_demo")
    ),
    path(
        "face/",
        include(
            ("django_deepface.urls", "django_deepface"), namespace="django_deepface"
        ),
    ),
]

# Serve media files in production
if settings.MEDIA_URL and settings.MEDIA_ROOT:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            },
        ),
    ]

# Fallback for DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
