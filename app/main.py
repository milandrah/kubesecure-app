from fastapi import FastAPI
from fastapi.responses import Response

from prometheus_client import Counter, generate_latest

from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from .models import SecurityEvent


app = FastAPI()

Base.metadata.create_all(bind=engine)

REQUESTS = Counter(
    "app_requests_total",
    "Total requests"
)


@app.get("/")
def root():
    REQUESTS.inc()
    return {"message": "KubeSecure Platform"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )


@app.post("/events")
def create_event():

    db: Session = SessionLocal()

    event = SecurityEvent(
        severity="HIGH",
        source="Falco",
        message="Suspicious shell detected"
    )

    db.add(event)
    db.commit()

    return {
        "status": "event stored"
    }