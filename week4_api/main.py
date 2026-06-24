"""Week 4 — APIs & JSON Contracts.

Lab: a tiny image-analysis API contract with three routes:
    GET  /health           -> service status + version (for monitoring)
    POST /analyse          -> accept an image URL + config, return detections
    GET  /results/{id}     -> retrieve a stored analysis result by id

The lesson of the week: write the *contract* (the request/response shapes) before the
implementation. Pydantic enforces the contract automatically and FastAPI documents it at /docs.

Run:
    pip install "fastapi[standard]" uvicorn
    uvicorn main:app --reload
    # then open http://127.0.0.1:8000/docs
"""

from __future__ import annotations

import datetime
import uuid
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI(title="UniVision Image Analysis API", version="0.1.0")

# In-memory store standing in for a database (Week 9 topic).
_RESULTS: Dict[str, "AnalyseResponse"] = {}


# ── Request & Response Models ──────────────────────────────────────────────────


class AnalyseRequest(BaseModel):
    image_url: HttpUrl
    model_name: str = "yolov8n"
    confidence_threshold: float = Field(default=0.5, ge=0.0, le=1.0)
    max_detections: Optional[int] = Field(default=10, gt=0)


class Box(BaseModel):
    x1: int
    y1: int
    x2: int
    y2: int


class Detection(BaseModel):
    label: str
    confidence: float = Field(ge=0.0, le=1.0)
    box: Box


class AnalyseResponse(BaseModel):
    result_id: str
    image_url: str
    detections: List[Detection]
    processing_time_ms: float
    created_at: str


# ── Routes ──────────────────────────────────────────────────────────────────


@app.get("/health")
def health():
    """Liveness/readiness probe used by monitoring."""
    return {"status": "ok", "version": app.version}


@app.post("/analyse", response_model=AnalyseResponse)
def analyse(request: AnalyseRequest):
    """Analyse an image (simulated) and store the structured result.

    In a real system this would download the image, run the detector named in `model_name`,
    filter by `confidence_threshold`, and cap the list at `max_detections`. Here we return a
    deterministic fake result so the contract can be tested end-to-end.
    """
    result_id = str(uuid.uuid4())

    detections = [
        Detection(label="person", confidence=0.92, box=Box(x1=50, y1=30, x2=200, y2=380)),
        Detection(label="helmet", confidence=0.78, box=Box(x1=70, y1=20, x2=160, y2=80)),
    ]
    # Honour the contract's knobs even on the simulated path.
    detections = [d for d in detections if d.confidence >= request.confidence_threshold]
    if request.max_detections is not None:
        detections = detections[: request.max_detections]

    response = AnalyseResponse(
        result_id=result_id,
        image_url=str(request.image_url),
        detections=detections,
        processing_time_ms=143.2,
        created_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    )
    _RESULTS[result_id] = response
    return response


@app.get("/results/{result_id}", response_model=AnalyseResponse)
def get_result(result_id: str):
    """Fetch a previously stored result, or 404 if the id is unknown."""
    result = _RESULTS.get(result_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Result not found")
    return result
