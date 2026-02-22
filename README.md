# Poetry-Pipeline


Secure FastAPI with Docker & CI/CD

---

## Project Overview

Poetry-Pipeline is a secure, production-ready FastAPI application packaged with Docker, designed following modern DevOps best practices. It includes:

- CI/CD automation via GitHub Actions
- Dependency management with Poetry
- Secure containerization (non-root user, read-only filesystem, resource limits)
- Logging, healthchecks, and observability
- Branch-based development workflow

This project demonstrates modern Python DevOps practices, from containerization to automated testing and deployment.

---

## Tech Stack

- Python 3.14
- FastAPI (API framework)
- Poetry (dependency management)
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- Pre-commit hooks (code quality & formatting)

---

## Features

| Feature               | Description                                                       |
|-----------------------|-------------------------------------------------------------------|
| Dockerized App         | Runs FastAPI in a secure container, using a non-root user.        |
| CI/CD Pipeline         | Automated linting, testing, and code coverage checks.            |
| Dependency Caching     | Speeds up builds with Poetry caching.                             |
| Healthchecks           | Monitors container health to ensure uptime.                      |
| Resource Limits        | CPU/memory caps to prevent runaway processes.                     |
| Logging & Observability| Rotating logs and structured logging for easier debugging.        |

---

## Project Structure
