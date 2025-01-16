import logging
import os

import uvicorn
from fastapi import FastAPI, HTTPException
from health_check_utils import HealthStatus, health_check

logging.basicConfig(level=logging.WARNING)

app = FastAPI()
health_status = HealthStatus()


@app.get("/")
@health_check(health_status=health_status)
def home():
    return "Connected"


@app.get("/health")
def health():
    if not health_status.healthy:
        raise HTTPException(
            status_code=health_status.status_code,
            detail=health_status.status_msg,
        )
    return {"detail": health_status.status_msg}
