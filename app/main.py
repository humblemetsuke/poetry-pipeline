import os
import socket

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Hello from DevOps MVP 🚀",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "dev"),
    }
