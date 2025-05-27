from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/demo/", permanent=True)),  # Redirect root to demo
    path("demo/", include("django_deepface_demo.urls", namespace="django_deepface_demo")),
    path("face/", include(("django_deepface.urls", "django_deepface"), namespace="django_deepface")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 