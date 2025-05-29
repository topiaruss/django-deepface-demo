# Production Deployment Guide

This guide explains how to deploy the Django DeepFace Demo application in production using Docker.

## Prerequisites

- Docker and Docker Compose installed
- A domain name (optional, for production)
- SSL certificate (optional, for HTTPS)

## Quick Start

1. **Copy and configure environment variables:**
   ```bash
   cp production.env.example .env
   # Edit .env file with your production values
   ```

2. **Build the Docker image:**
   ```bash
   make prod-build
   ```

3. **Start the application:**
   ```bash
   make prod-up
   ```

4. **Create a superuser (first time only):**
   ```bash
   docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
   ```

The application will be available at:
- http://localhost (nginx)
- http://localhost:8000 (direct Django/Gunicorn access)

## Configuration

### Environment Variables

Edit the `.env` file with your production settings:

- `POSTGRES_PASSWORD`: Strong password for PostgreSQL
- `DJANGO_SECRET_KEY`: Generate a new secret key for production
- `DJANGO_DEBUG`: Set to `False` for production
- `DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `WEB_PORT`: Port for the Django application (default: 8000)
- `NGINX_PORT`: Port for Nginx (default: 80)

### Generate a Secret Key

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Management Commands

### View logs:
```bash
make prod-logs
```

### Stop the application:
```bash
make prod-down
```

### Access the web container shell:
```bash
make prod-shell
```

### Run Django management commands:
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py <command>
```

## Architecture

The production setup includes:

1. **PostgreSQL with pgvector**: Database with vector search capabilities
2. **Django/Gunicorn**: Application server
3. **Nginx**: Reverse proxy and static file server

## Data Persistence

- PostgreSQL data is stored in a named volume `postgres_data`
- Media files are stored in `./media` directory
- Static files are collected to a Docker volume

## Backup and Restore

### Backup database:
```bash
docker-compose -f docker-compose.prod.yml exec db pg_dump -U postgres deepface > backup.sql
```

### Restore database:
```bash
docker-compose -f docker-compose.prod.yml exec -T db psql -U postgres deepface < backup.sql
```

## Security Considerations

1. Always use strong passwords in production
2. Set `DJANGO_DEBUG=False`
3. Configure `DJANGO_ALLOWED_HOSTS` properly
4. Use HTTPS in production (configure SSL in nginx)
5. Regularly update Docker images and dependencies
6. Implement proper firewall rules

## Troubleshooting

### Database connection issues:
- Check if the database container is healthy: `docker-compose -f docker-compose.prod.yml ps`
- View database logs: `docker-compose -f docker-compose.prod.yml logs db`

### Static files not loading:
- Ensure static files are collected: `docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic`
- Check nginx configuration and volumes

### Application errors:
- Check Django logs: `docker-compose -f docker-compose.prod.yml logs web`
- Access shell for debugging: `make prod-shell` 