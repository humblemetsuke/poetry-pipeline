# Poetry-Pipeline

Secure FastAPI with Docker & CI/CD

---

## Badges

<!-- Add your badges here -->
<!-- Example: CI/CD -->
![CI](https://github.com/humblemetsuke/poetry-pipeline/actions/workflows/ci-cd.yml/badge.svg)
<!-- Docker Hub -->
![Docker](https://img.shields.io/docker/v/<your-dockerhub-username>/poetry-pipeline)
<!-- GitHub Container Registry -->
![GHCR](https://img.shields.io/badge/GHCR-ready-blue)
<!-- Version -->
![Version](https://img.shields.io/badge/version-0.1.0-blue)

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

| Feature                 | Description                                                |
|-------------------------|------------------------------------------------------------|
| Dockerized App          | Runs FastAPI in a secure container using a non-root user. |
| CI/CD Pipeline          | Automated linting, testing, and code coverage checks.     |
| Dependency Caching      | Speeds up builds with Poetry caching.                     |
| Healthchecks            | Monitors container health to ensure uptime.               |
| Resource Limits         | CPU/memory caps to prevent runaway processes.             |
| Logging & Observability | Rotating logs and structured logging for easier debugging.|

---

## Project Structure
