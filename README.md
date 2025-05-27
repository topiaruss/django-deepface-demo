# Django DeepFace Demo

A Django application that demonstrates face recognition and authentication using DeepFace.

## Features

- Face-based user authentication
- Device tracking and statistics
- Admin interface for monitoring
- Secure image handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/django-deepface-demo.git
cd django-deepface-demo
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Visit http://localhost:8000/admin/ to access the admin interface
2. Create a user profile and upload a face image
3. Use the face login feature at http://localhost:8000/face-login/
4. View device statistics at http://localhost:8000/demo/device-stats/

## Testing

Run all tests:
```bash
make test-all
```

Run specific tests:
```bash
make test-specific test="django_deepface_demo/tests/test_deepface_suite.py -v"
```

## License

MIT