.PHONY: init run test-all test-specific clean db-migrate package-install package-uninstall package-test package-build

# Initialize virtual environment and install dependencies
init:
	python -m venv .venv
	. .venv/bin/activate && pip install uv
	. .venv/bin/activate && uv pip install -r requirements.txt

# Run Django development server
run:
	. .venv/bin/activate && python manage.py runserver

# Run all tests
test-all:
	. .venv/bin/activate && pytest --ff  --cov=django_deepface --cov-report=html

test-all-first:
	. .venv/bin/activate && pytest --ff -x 

# Run specific test
test-specific:
	. .venv/bin/activate && pytest $(test)

# Create and apply database migrations
db-migrate:
	. .venv/bin/activate && python manage.py makemigrations
	. .venv/bin/activate && python manage.py migrate

# Package development commands
package-install:
	. .venv/bin/activate && uv pip install -e ./django-deepface-package

package-uninstall:
	. .venv/bin/activate && uv pip uninstall django-deepface -y

package-test:
	. .venv/bin/activate && cd django-deepface-package && pytest

package-build:
	. .venv/bin/activate && cd django-deepface-package && python -m build

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