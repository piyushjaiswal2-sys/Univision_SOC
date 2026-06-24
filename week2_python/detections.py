"""Week 2 — Python As A Tool.

Lab: represent detections as dictionaries and filter them by confidence.

A single *detection* is the smallest unit of output from the vision pipeline. We model it as a
plain dictionary so it is trivial to turn into JSON later (Week 4 API) and easy to inspect by eye.

Run directly to see a small demo:

    python detections.py
"""

from __future__ import annotations

from typing import List, Optional, TypedDict


class Box(TypedDict):
    """Axis-aligned bounding box in pixel coordinates."""

    x1: int
    y1: int
    x2: int
    y2: int


class Detection(TypedDict):
    """One detected object: what it is, how sure we are, and where it is."""

    label: str
    confidence: float
    box: Box


def make_detection(label: str, confidence: float, box: Box) -> Detection:
    """Build one detection, validating the confidence is a probability in [0, 1]."""
    if not 0.0 <= confidence <= 1.0:
        raise ValueError(f"confidence must be in [0, 1], got {confidence}")
    return {"label": label, "confidence": confidence, "box": box}


def average_confidence(scores: List[float]) -> float:
    """Return the mean of a list of confidence scores.

    Returns 0.0 for an empty list so callers never divide by zero.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def filter_by_confidence(
    detections: List[Detection], threshold: float = 0.5
) -> List[Detection]:
    """Keep only detections whose confidence is >= threshold.

    This is the core "trust gate" of the pipeline: low-confidence guesses are dropped before
    they ever reach the dashboard or trigger an alert.
    """
    if not 0.0 <= threshold <= 1.0:
        raise ValueError(f"threshold must be in [0, 1], got {threshold}")
    return [d for d in detections if d["confidence"] >= threshold]


def top_detection(detections: List[Detection]) -> Optional[Detection]:
    """Return the single most confident detection, or None if the list is empty."""
    if not detections:
        return None
    return max(detections, key=lambda d: d["confidence"])


def _demo() -> None:
    detections: List[Detection] = [
        make_detection("person", 0.92, {"x1": 50, "y1": 30, "x2": 200, "y2": 380}),
        make_detection("helmet", 0.78, {"x1": 70, "y1": 20, "x2": 160, "y2": 80}),
        make_detection("bag", 0.41, {"x1": 210, "y1": 250, "x2": 300, "y2": 360}),
        make_detection("phone", 0.33, {"x1": 120, "y1": 300, "x2": 150, "y2": 340}),
    ]

    print(f"Total detections        : {len(detections)}")
    print(f"Average confidence      : {average_confidence([d['confidence'] for d in detections]):.3f}")

    kept = filter_by_confidence(detections, threshold=0.5)
    print(f"Kept at threshold 0.50  : {[d['label'] for d in kept]}")

    best = top_detection(detections)
    print(f"Most confident          : {best['label']} ({best['confidence']:.2f})")


if __name__ == "__main__":
    _demo()
