# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django demonstration application showcasing face recognition authentication using the `django-deepface` library. The app provides both traditional password authentication and face recognition login, with device statistics tracking for viability analysis.

## Key Architecture

- **Django 5.2** web application with PostgreSQL + pgvector for vector similarity search
- **Two-app structure**:
  - `django_deepface_demo`: Demo app with device tracking and statistics views
  - `django_deepface`: Face recognition package (installed as dependency)
- **Face recognition workflow**: Users upload face images via webcam/file, which are processed and stored for subsequent authentication
- **Device tracking**: Captures browser, OS, and device information during face capture for analytics

## Essential Commands

### Development Setup
```bash
# Full initialization (creates .venv and installs dependencies)
make init

# Install development dependencies
make install-dev

# Database setup (Docker)
make db-up
make db-migrate

# Create superuser
make csu

# Run development server
make run
```

### Dependency Management
```bash
# Add new dependency
uv add package-name

# Add development dependency
uv add --group dev package-name

# Remove dependency
uv remove package-name

# Sync dependencies (like npm install)
uv sync
```

### Testing
```bash
# Run all tests with coverage
make test-all

# Run first failure only
make test-all-first

# Run specific test
make test-specific test="path/to/test.py -v"
```

### Database Management
```bash
# Reset database completely
make db-reset

# Manual migrations
make db-migrate
```

### Production Deployment
```bash
# Production Docker build and run
make prod-build
make prod-up
make prod-logs
```

## Database Configuration

The application requires PostgreSQL with the pgvector extension for face embedding similarity search. Database connection is configured via `DATABASE_URL` environment variable in `.env` file.

## URL Structure

- `/admin/` - Django admin interface
- `/demo/` - Main demo application (redirects from root)
- `/face/` - Face recognition authentication (from django-deepface package)
- `/demo/device-stats/` - Device statistics dashboard (staff only)

## Key Models

- `CaptureDevice` (`django_deepface_demo/models.py:4`): Tracks device information and success rates for face capture attempts
- Face-related models are provided by the `django-deepface` package

## Testing Configuration

pytest is configured with coverage reporting to `htmlcov/`. Tests are organized with markers: `slow`, `integration`, `unit`. The test suite covers the django-deepface package functionality.

## Environment Variables

Required in `.env`:
- `DATABASE_URL`: PostgreSQL connection string
- `DJANGO_SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode setting