from django.apps import AppConfig


class DjangoDeepfaceDemoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_deepface_demo"

    def ready(self):
        """Import and connect signal handlers when the app is ready."""
        print("READY")
        from django_deepface.signals import face_image_processed  # noqa
        from django_deepface_demo.signals import handle_face_image_processed  # noqa

        assert face_image_processed is not None
        assert handle_face_image_processed is not None
        face_image_processed.connect(handle_face_image_processed)
