.PHONY: init run test-all test-specific clean db-migrate package-install package-uninstall package-test package-build db-up db-down db-reset prod-build prod-up prod-down prod-logs prod-shell sync install-dev install-prod helm-lint helm-template helm-install helm-upgrade helm-uninstall helm-package

# Initialize project with uv
init:
	uv sync

# Install development dependencies
install-dev:
	uv sync --extra dev

# Install production dependencies only
install-prod:
	uv sync --extra prod --no-dev

# Sync dependencies (equivalent to npm install)
sync:
	uv sync

# Run Django development server
csu:
	uv run python manage.py createsuperuser

run:
	uv run python manage.py runserver

# Run all tests
test-all:
	uv run pytest --ff --cov=django_deepface_demo --cov-report=html django_deepface_demo/tests

test-all-first:
	uv run pytest --ff -x 

# Run specific test
test-specific:
	uv run pytest $(test)

# Create and apply database migrations
db-migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate

# Database management with Docker
db-up:
	docker-compose up -d

db-down:
	docker-compose down

db-reset:
	docker-compose down -v
	docker-compose up -d
	sleep 3  # Wait for database to be ready
	make db-migrate

# Package development commands
package-install:
	uv add --editable ./django-deepface-package

package-uninstall:
	uv remove django-deepface

package-test:
	cd django-deepface-package && uv run pytest

package-build:
	cd django-deepface-package && uv build

# Clean up Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".coverage" -exec rm -r {} +
	find . -type d -name "htmlcov" -exec rm -r {} +
	find . -type d -name ".mypy_cache" -exec rm -r {} +
	find . -type d -name ".ruff_cache" -exec rm -r {} +
	find . -type d -name ".hypothesis" -exec rm -r {} +

# Production deployment targets
prod-build:
	DOCKER_DEFAULT_PLATFORM=linux/amd64 NGINX_PORT=80 docker-compose -f docker-compose.prod.yml build

prod-up:
	docker-compose -f docker-compose.prod.yml up -d

prod-down:
	docker-compose -f docker-compose.prod.yml down

prod-logs:
	docker-compose -f docker-compose.prod.yml logs -f

prod-shell:
	docker-compose -f docker-compose.prod.yml exec web bash

# Kubernetes/Helm deployment targets
helm-lint:
	helm lint helm/django-deepface-demo

helm-template:
	helm template django-deepface-demo helm/django-deepface-demo

helm-install:
	helm install django-deepface-demo helm/django-deepface-demo \
		--create-namespace \
		--namespace django-deepface-demo

helm-upgrade:
	helm upgrade django-deepface-demo helm/django-deepface-demo \
		--namespace django-deepface-demo

helm-uninstall:
	helm uninstall django-deepface-demo --namespace django-deepface-demo

helm-package:
	helm package helm/django-deepface-demo