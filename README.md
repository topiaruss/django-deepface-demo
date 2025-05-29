# Django DeepFace Demo

A Django application that demonstrates face recognition and authentication using my [django-deepface](https://github.com/topiaruss/django-deepface) library.

## Features

- 🔐 Face recognition authentication alongside traditional password authentication
- 📸 Capture face images via webcam or file upload
- ⏱️ Webcam device tracking and statistics - to prevew viability in your org
- 🚀 Fast face matching using pgvector similarity search
- 👤 Support for multiple face images per user (up to 4)
- 🎨 Modern, responsive UI with Bootstrap 5
- 🔒 Secure storage and processing of biometric data

## Installation

1. Clone the repository:
```bash
git clone https://github.com/topiaruss/django-deepface-demo.git
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

4. Set up PostgreSQL with pgvector:

   **Option 1: Using Docker (Recommended)**
   ```bash
   make db-up
   ```
   This will start a PostgreSQL database with pgvector extension pre-installed.

   **Option 2: Manual Installation**
   - Install PostgreSQL if not already installed
   - Install the pgvector extension:
     ```bash
     # On macOS with Homebrew
     brew install pgvector
     
     # On Ubuntu/Debian
     sudo apt install postgresql-16-pgvector
     
     # On other systems, see: https://github.com/pgvector/pgvector#installation
     ```
   - Create a database and enable the extension:
     ```sql
     CREATE DATABASE deepface;
     CREATE EXTENSION IF NOT EXISTS vector;
     ```

5. Configure database connection:
   - Create a `.env` file in the project root:
     ```bash
     DATABASE_URL=postgresql://postgres:postgres@localhost:5432/deepface
     ```
   - If using manual PostgreSQL installation, adjust the connection string accordingly

6. Run migrations:
```bash
make db-migrate
```

7. Create a superuser:
```bash
make csu
```

8. Run the development server:
```bash
make run
```

## Usage

1. Visit http://localhost:8000/face/login/ to do the initial login
2. Follow the profile link and upload a face image, using your webcam if you like
3. Logout, then login with the face login feature at http://localhost:8000/face/login/
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

## Production Deployment

For production deployment using Docker, see [DEPLOYMENT.md](DEPLOYMENT.md).