# Django DeepFace Demo Helm Chart

This Helm chart deploys the Django DeepFace Demo application to a Kubernetes cluster.

## Prerequisites

- Kubernetes 1.19+
- Helm 3.x
- A container registry with the application image

## Installation

### Quick Start

1. Add the PostgreSQL Helm repository (for the dependency):
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

2. Install the chart:
```bash
helm install django-deepface-demo ./helm/django-deepface-demo \
  --set image.repository=your-registry/django-deepface-demo \
  --set image.tag=latest \
  --create-namespace \
  --namespace django-deepface-demo
```

### Custom Configuration

Create a `values.yaml` file with your custom configuration:

```yaml
image:
  repository: your-registry/django-deepface-demo
  tag: "latest"

ingress:
  enabled: true
  className: "nginx"
  hosts:
    - host: deepface.example.com
      paths:
        - path: /
          pathType: Prefix

django:
  allowedHosts: "deepface.example.com"
  
postgresql:
  auth:
    postgresPassword: "secure-password"

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 250m
    memory: 256Mi
```

Then install with:
```bash
helm install django-deepface-demo ./helm/django-deepface-demo -f values.yaml
```

## Configuration

### Key Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `image.repository` | Container image repository | `django-deepface-demo` |
| `image.tag` | Container image tag | `""` (uses appVersion) |
| `image.pullPolicy` | Image pull policy | `IfNotPresent` |
| `replicaCount` | Number of replicas | `1` |
| `service.type` | Kubernetes service type | `ClusterIP` |
| `service.port` | Service port | `8000` |
| `ingress.enabled` | Enable ingress | `false` |
| `ingress.className` | Ingress class name | `""` |
| `django.debug` | Django DEBUG setting | `false` |
| `django.secretKey` | Django SECRET_KEY | `""` (auto-generated) |
| `django.allowedHosts` | Django ALLOWED_HOSTS | `"*"` |
| `postgresql.enabled` | Enable PostgreSQL dependency | `true` |
| `postgresql.auth.postgresPassword` | PostgreSQL password | `"postgres"` |
| `postgresql.auth.database` | PostgreSQL database name | `"deepface"` |

### Database Configuration

#### Using the included PostgreSQL

The chart includes a PostgreSQL dependency that's enabled by default:

```yaml
postgresql:
  enabled: true
  auth:
    postgresPassword: "your-password"
    database: "deepface"
```

#### Using an external database

To use an external PostgreSQL database:

```yaml
postgresql:
  enabled: false

django:
  database:
    external: true
    host: "external-postgres.example.com"
    port: 5432
    name: "deepface"
    user: "postgres"
    password: "password"
```

### Storage

The application requires persistent storage for media files:

```yaml
django:
  media:
    size: 10Gi
    storageClass: "fast-ssd"  # Optional
```

### Scaling

Enable horizontal pod autoscaling:

```yaml
autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
```

## Upgrading

```bash
helm upgrade django-deepface-demo ./helm/django-deepface-demo -f values.yaml
```

## Uninstalling

```bash
helm uninstall django-deepface-demo --namespace django-deepface-demo
```

## Troubleshooting

### Check pod status
```bash
kubectl get pods -n django-deepface-demo
kubectl describe pod <pod-name> -n django-deepface-demo
```

### View logs
```bash
kubectl logs -n django-deepface-demo deployment/django-deepface-demo
```

### Access the database
```bash
kubectl exec -it -n django-deepface-demo deployment/django-deepface-demo-postgresql -- psql -U postgres -d deepface
```

### Run Django management commands
```bash
kubectl exec -it -n django-deepface-demo deployment/django-deepface-demo -- python manage.py shell
kubectl exec -it -n django-deepface-demo deployment/django-deepface-demo -- python manage.py createsuperuser
```