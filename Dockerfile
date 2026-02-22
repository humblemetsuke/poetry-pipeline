# =======================================
# Secure DevOps-Ready FastAPI Dockerfile
# =======================================

# ===========================
# Base Image: Python 3.12 slim
# ===========================

# Use SHA digest to guarantee immutability and reproducibility.
FROM python@sha256:4a8e0824201e50fc44ee8d208a2b3e44f33e00448907e524066fca5a96eb5567

# ======================
# Environment variables
# ======================

# Prevent .pyc files from being created
ENV PYTHONDONTWRITEBYTECODE=1

# Flush output instantly
ENV PYTHONUNBUFFERED=1

# Container is in production mode
ENV ENVIRONMENT=production

# Poetry configs: no virtualenv, non-interactive, no ANSI colors
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_NO_INTERACTION=1
ENV POETRY_NO_ANSI=1

# ---------------------------
# Set working directory
# ---------------------------
WORKDIR /app

# ---------------------------
# Install Poetry
# ---------------------------
RUN pip install --no-cache-dir poetry==1.7.0

# ---------------------------
# Dependency caching
# ---------------------------
COPY pyproject.toml poetry.lock* ./

# Install only production dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# ---------------------------
# Copy application code
# ---------------------------
COPY app ./app

# ---------------------------
# Add non-root user (security)
# ---------------------------
RUN useradd -m appuser
USER appuser

# ---------------------------
# Expose port
# ---------------------------
EXPOSE 8000

# ---------------------------
# Healthcheck
# ---------------------------
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
  CMD curl -f http://localhost:8000/health || exit 1

# ======================
# Run FastAPI app
# ======================
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
