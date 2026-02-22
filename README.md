# Poetry-Pipeline

![CI](https://github.com/humblemetsuke/poetry-pipeline/actions/workflows/ci-cd.yml/badge.svg)

Secure FastAPI with Docker & CI/CD

---

## Project Overview

Poetry-Pipeline is a secure, production-ready FastAPI application packaged with Docker, designed following DevOps best practices. It features:

- CI/CD with GitHub Actions
- Dependency management via Poetry
- Docker security best practices (non-root user, read-only filesystem, resource limits)
- Logging, healthchecks, and observability
- Branch-based development workflow

This project demonstrates modern Python DevOps practices, from containerization to automated testing and deployment.

---

## Tech Stack

- Python 3.14
- FastAPI (API framework)
- Poetry (dependency management)
- Docker & Docker Compose (containerization)
- GitHub Actions (CI/CD)
- Pre-commit hooks (code quality & formatting)

---

## Features

| Feature | Description |
|---------|-------------|
| Dockerized App | Runs FastAPI in a secure container, using a non-root user. |
| CI/CD Pipeline | Automated linting, testing, and code coverage checks. |
| Dependency Caching | Speeds up builds with Poetry caching. |
| Healthchecks | Monitors container health to ensure uptime. |
| Resource Limits | CPU/memory caps to prevent runaway processes. |
| Logging & Observability | Rotating logs and structured logging for easier debugging. |




---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/humblemetsuke/poetry-pipeline.git
cd poetry-pipeline

# Build the container

docker build -t poetry-pipeline .

# Run the Container
docker run -p 8000:8000 poetry-pipeline

Check the health endpoint:
curl http://localhost:8000/health

Using Docker Compose (dev)

docker-compose up --build

CI/CD Pipeline

The GitHub Actions workflow automatically:

Installs dependencies via Poetry

Runs linting & pre-commit checks

Executes tests and checks coverage

Builds Docker images with caching

Performs healthchecks on the container

Branch & Git Workflow

Feature Branches: Used for new functionality (e.g., feat/docker-compose)

Merge to Main: Only after CI/CD passes and code review

Main Branch: Always production-ready

🎯 Key Learnings

Building secure Docker images for Python apps

Automating CI/CD pipelines for fast, reliable deployments

Managing dependencies reproducibly with Poetry

Observability & fault tolerance in containerized environments

📌 Next Steps

Deploy the container to a cloud service (Render, Railway, AWS ECS)

Add more FastAPI endpoints with tests

Integrate automated vulnerability scanning (Snyk, Trivy)
---

## Project Structure
