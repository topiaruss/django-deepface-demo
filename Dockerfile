# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libglib2.0-0 \
    libgl1-mesa-glx \
    netcat-traditional \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install uv for faster package installation
RUN pip install uv

# Copy project files
COPY . .

# Store git commit hash
RUN git rev-parse --short HEAD > .git_commit || echo "unknown" > .git_commit

# Install Python dependencies using uv
RUN uv sync --frozen --no-dev

# Activate the virtual environment by adding it to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Pre-download DeepFace models to avoid runtime downloads
# Commented out for cross-platform builds - models will download at runtime
# RUN uv run python -c "from deepface import DeepFace; DeepFace.build_model('VGG-Face')"

# Make entrypoint script executable
RUN chmod +x /app/docker-entrypoint.sh

# Create media directory
RUN mkdir -p /app/media

# Set the entrypoint
ENTRYPOINT ["/app/docker-entrypoint.sh"]

# Run gunicorn
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "django_deepface_demo.wsgi:application"] 
