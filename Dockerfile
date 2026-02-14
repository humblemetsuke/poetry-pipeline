# =======================================
# Secure DevOps-Ready FastAPI Dockerfile
# =======================================

# ===========================
# Base Image: Minimal Python
# ============================

# Use a SHA digest to ensure immutability and prevent image tampering.
# Also provides reproducibility, ensuring it avoids any "worked on my machine" issues.
FROM python@sha256:0b23cfb7425d065008b778022a17b1551c82f8b4866ee5a7a200084b7e2eafbf

# ======================
# Environment variables
# ======================


# Prevents bloating the image with additional files (.pyc files).
ENV PYTHONDONTWRITEBYTECODE=1

# Flushes output instantly, eliminates delays, aids in debugging.
ENV PYTHONBUFFERED=1

# Assigns environment variable, signifying container is in production mode.
ENV ENVIRONMENT=production

# Eliminates additional poetry venv in container that causes bloat.
ENV POETRY_VIRTUALENVS_CREATE=false

# Eliminates need for user input, allowing for full automation.
ENV POETRY_NO_INTERACTION=1

# Disables coloured output from Poetry. Keeps CI/CD logs predictable.
ENV POETRY_NO_ANSI=1

# ---------------------------
# Add non-root user (security)
# ---------------------------

# Stripping root access minimises harm by malicious user.

RUN useradd -m appuser
USER appuser
