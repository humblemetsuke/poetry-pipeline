# =======================================
# Secure DevOps-Ready FastAPI Dockerfile
# =======================================

FROM python@sha256:4a8e0824201e50fc44ee8d208a2b3e44f33e00448907e524066fca5a96eb5567

# ---------------------------
# Environment variables
# ---------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=production
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_NO_INTERACTION=1
ENV POETRY_NO_ANSI=1

# ---------------------------
# Install OS dependencies
# ---------------------------
USER root
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

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
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# ---------------------------
# Copy application code
# ---------------------------
COPY app ./app

# ---------------------------
# Add non-root user
# ---------------------------
RUN useradd -m appuser
RUN mkdir -p /tmp && chown appuser:appuser /tmp
USER appuser

# ---------------------------
# Expose port
# ---------------------------
EXPOSE 8000

# ---------------------------
# Healthcheck (tolerant)
# ---------------------------
HEALTHCHECK --interval=10s --timeout=5s --start-period=30s --retries=10 \
  CMD curl -f http://localhost:8000/health || exit 1

# ---------------------------
# Run FastAPI
# ---------------------------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"]
