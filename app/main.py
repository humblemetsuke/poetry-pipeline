import logging
import os
import socket
from logging.handlers import RotatingFileHandler

import structlog
from fastapi import FastAPI

ENV = os.getenv("ENVIRONMENT", "dev")
# -----------------------------
# Ensure log folder exists
# -----------------------------
os.makedirs("logs", exist_ok=True)
log_file = "logs/poetry-pipeline.log"


# -----------------------------
# Rotating file handler
# -----------------------------
file_handler = RotatingFileHandler(
    filename=log_file,
    maxBytes=5 * 1024 * 1024,
    backupCount=3,
    encoding="utf-8",
)
file_handler.setFormatter(logging.Formatter("%(message)s"))

# -----------------------------
# Console handler
# -----------------------------
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(message)s"))

# -----------------------------
# Standard logging config
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    handlers=[file_handler, console_handler],
)

# -----------------------------
# Structlog config
# -----------------------------
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ]
)
logger = structlog.get_logger()
logger.info("Logging setup complete! Both file and console active.")

# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI()


@app.get("/")
def read_root():
    logger.info(
        "endpoint_called",
        endpoint="/",
        hostname=socket.gethostname(),
        environment=ENV,
    )
    return {
        "message": "Hello from DevOps MVP 🚀",
        "hostname": socket.gethostname(),
        "environment": ENV,
    }


@app.get("/health")
def health_check():
    logger.info(
        "endpoint_called",
        endpoint="/health",
        hostname=socket.gethostname(),
        environment=ENV,
        status_code="ok",
    )
    return {"status": "ok"}
