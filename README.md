# Poetry-Pipeline






Secure FastAPI with Docker & CI/CD

Poetry-Pipeline is a secure, production-ready FastAPI application packaged with Docker, designed following modern DevOps best practices. It includes CI/CD automation, dependency caching, observability, and secure containerization.

🚀 Project Overview

CI/CD: Automated workflow via GitHub Actions

Dependency Management: Poetry ensures reproducible builds

Secure Docker: Non-root user, read-only filesystem, CPU/memory limits

Logging & Healthchecks: Rotating logs, container health monitoring

Branch-based Workflow: Feature branches for new functionality

This project demonstrates modern Python DevOps practices from containerization to automated testing and deployment.

🛠 Tech Stack

Python 3.14

FastAPI (API framework)

Poetry (dependency management)

Docker & Docker Compose (containerization)

GitHub Actions (CI/CD)

Pre-commit hooks (code quality & formatting)

✨ Features
Feature	Description
Dockerized App	Runs FastAPI in a secure container, using a non-root user.
CI/CD Pipeline	Automated linting, testing, and code coverage checks.
Dependency Caching	Speeds up builds with Poetry caching.
Healthchecks	Monitors container health to ensure uptime.
Resource Limits	CPU/memory caps to prevent runaway processes.
Logging & Observability	Rotating logs and structured logging for easier debugging.
📂 Project Structure
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
🏗 CI/CD Pipeline

The GitHub Actions workflow automatically:

Installs dependencies via Poetry

Runs linting & pre-commit checks

Executes tests and checks coverage

Builds Docker images with caching

Performs healthchecks on the container

🌿 Branch & Git Workflow

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
