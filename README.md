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


## Deployment Options

### Docker Deployment
For a production-like deployment using Docker, see [DEPLOYMENT.md](DEPLOYMENT.md).

### Kubernetes Deployment
For Kubernetes deployment using Helm, see the [Kubernetes Deployment](#kubernetes-deployment) section below.


## Installation

1. Clone the repository:
```bash
git clone https://github.com/topiaruss/django-deepface-demo.git
cd django-deepface-demo
```

2. Install uv if you don't have it:
```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

3. Initialize the project (creates virtual environment and installs dependencies):
```bash
make init
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

## Dependency Management

This project uses [uv](https://github.com/astral-sh/uv) for fast Python package management:

- **Development dependencies**: `make install-dev` or `uv sync --extra dev`
- **Production dependencies**: `make install-prod` or `uv sync --extra prod --no-dev`
- **Add new dependencies**: `uv add package-name`
- **Remove dependencies**: `uv remove package-name`
- **Update dependencies**: `uv sync`

## Usage

1. Visit http://localhost:8000/face/login/ to do the initial login
2. Follow the profile link and upload a face image, using your webcam if you like
3. Logout, then login with the face login feature at http://localhost:8000/face/login/
4. View device statistics at http://localhost:8000/demo/device-stats/

### Device Statistics Dashboard

The application includes a comprehensive device statistics dashboard that helps you understand how users are accessing the face recognition features:

![Device Statistics Dashboard](DeviceStats.webp)

This dashboard provides valuable insights into:
- **Browser Usage**: See which browsers (Chrome, Firefox, Safari, etc.) are being used for face capture
- **Device Types**: Track whether users are on desktop, mobile, or tablet devices
- **Operating Systems**: Monitor the distribution of Windows, macOS, Linux, iOS, and Android users
- **Success Rates**: Analyze face recognition success rates across different platforms

This information is particularly useful for:
- Understanding your user base's technical capabilities
- Identifying potential compatibility issues with specific browsers or devices
- Making informed decisions about which platforms to prioritize for support
- Predicting success of face authentication in your organization

## Testing

Run all tests:
```bash
make test-all
```

Run specific tests:
```bash
make test-specific test="django_deepface_demo/tests/test_deepface_suite.py -v"
```

## Kubernetes Deployment

This project includes a Helm chart for easy deployment to Kubernetes clusters.

### Prerequisites

- Kubernetes cluster (1.19+)
- Helm 3.x installed
- kubectl configured to access your cluster
- Container registry access to push the application image

### Building and Pushing the Docker Image

First, build and push the application image to your container registry:

```bash
# Build the image (you'll need to update the image name/tag)
docker build -t your-registry/django-deepface-demo:latest .

# Push to your registry
docker push your-registry/django-deepface-demo:latest
```

### Helm Deployment Commands

```bash
# Validate the Helm chart
make helm-lint

# Preview the generated Kubernetes manifests
make helm-template

# Install the application
make helm-install

# Upgrade an existing installation
make helm-upgrade

# Uninstall the application
make helm-uninstall
```

### Custom Configuration

Create a custom `values.yaml` file to override default settings:

```yaml
# custom-values.yaml
image:
  repository: your-registry/django-deepface-demo
  tag: "latest"

ingress:
  enabled: true
  className: "nginx"
  hosts:
    - host: deepface.yourdomain.com
      paths:
        - path: /
          pathType: Prefix

django:
  allowedHosts: "deepface.yourdomain.com"

postgresql:
  auth:
    postgresPassword: "your-secure-password"

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 250m
    memory: 256Mi
```

Then deploy with custom values:

```bash
helm install django-deepface-demo helm/django-deepface-demo \
  -f custom-values.yaml \
  --create-namespace \
  --namespace django-deepface-demo
```

### Accessing the Application

After deployment, you can access the application:

```bash
# Port forward to access locally
kubectl port-forward -n django-deepface-demo svc/django-deepface-demo 8000:8000

# Or check ingress (if enabled)
kubectl get ingress -n django-deepface-demo
```

The application will be available at http://localhost:8000/demo/

### Monitoring and Logs

```bash
# View pods
kubectl get pods -n django-deepface-demo

# View logs
kubectl logs -n django-deepface-demo deployment/django-deepface-demo

# View PostgreSQL logs
kubectl logs -n django-deepface-demo deployment/django-deepface-demo-postgresql
```

## License

MIT

