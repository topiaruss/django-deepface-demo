import os
import pytest
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

@pytest.fixture
def client():
    from django.test import Client
    return Client()

@pytest.fixture
def real_face_image():
    """Fixture that provides a real test image file."""
    # Create a test image file
    image_path = os.path.join(os.path.dirname(__file__), "test_face.webp")

    # Read the image file
    with open(image_path, "rb") as f:
        image_content = f.read()

    # Create a SimpleUploadedFile
    return SimpleUploadedFile(
        name="test_face.webp", content=image_content, content_type="image/webp"
    ) 