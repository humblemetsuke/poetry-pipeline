# poetry-pipeline
Poetry-Pipeline: Secure FastAPI with Docker & CI/CD

Project Overview

Poetry-Pipeline is a secure, production-ready FastAPI application packaged with Docker, designed for DevOps best practices. It features:

CI/CD with GitHub Actions

Dependency management via Poetry

Docker security best practices (non-root user, read-only filesystem, resource limits)

Logging, healthchecks, and observability

Branch-based development workflow

This project demonstrates modern Python DevOps practices, from containerization to automated testing and deployment.

Tech Stack

Python 3.14

FastAPI (API framework)

Poetry (dependency management)

Docker & Docker Compose (containerization)

GitHub Actions (CI/CD)

Pre-commit hooks (code quality & formatting)

Features

Feature	Description
Dockerized App	Runs FastAPI in a secure container, using a non-root user.
CI/CD Pipeline	Automated linting, testing, and code coverage checks.
Dependency Caching	Speeds up builds with Poetry caching.
Healthchecks	Monitors container health to ensure uptime.
Resource Limits	CPU/memory caps to prevent runaway processes.
Logging & Observability	Rotating logs and structured logging for easier debugging.


Project Structure
poetry-pipeline/
├─ app/                   # FastAPI application code
├─ Dockerfile             # Production-ready Dockerfile
├─ docker-compose.yml     # Local development & testing
├─ pyproject.toml         # Poetry dependency configuration
├─ poetry.lock            # Locked dependencies
├─ .github/workflows/ci-cd.yml  # CI/CD pipeline
└─ README.md              # Project documentation
⚙️ Getting Started
1. Clone the repository
git clone https://github.com/humblemetsuke/poetry-pipeline.git
cd poetry-pipeline
2. Build Docker container
docker build -t poetry-pipeline .
3. Run the container
docker run -p 8000:8000 poetry-pipeline

Check the health endpoint:

curl http://localhost:8000/health
4. Using Docker Compose (dev)
docker-compose up --build
CI/CD Pipeline

The GitHub Actions workflow automatically:

Installs dependencies via Poetry

Runs linting & pre-commit checks

Executes tests and checks coverage

Builds Docker images with caching

Performs healthchecks on the container
