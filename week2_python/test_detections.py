"""Week 2 Homework — tests for the confidence-threshold filter.

Tests prove that the small pieces behave as expected *before* the system grows complicated.

Run:
    pytest test_detections.py -v
"""

import pytest

from detections import (
    average_confidence,
    filter_by_confidence,
    make_detection,
    top_detection,
)


def sample_detections():
    return [
        make_detection("person", 0.92, {"x1": 50, "y1": 30, "x2": 200, "y2": 380}),
        make_detection("helmet", 0.78, {"x1": 70, "y1": 20, "x2": 160, "y2": 80}),
        make_detection("bag", 0.41, {"x1": 210, "y1": 250, "x2": 300, "y2": 360}),
        make_detection("phone", 0.33, {"x1": 120, "y1": 300, "x2": 150, "y2": 340}),
    ]


# ── average_confidence ────────────────────────────────────────────────────────

def test_average_confidence_basic():
    assert average_confidence([0.2, 0.4, 0.6]) == pytest.approx(0.4)


def test_average_confidence_empty_is_zero():
    assert average_confidence([]) == 0.0


# ── filter_by_confidence ──────────────────────────────────────────────────────

def test_filter_keeps_only_high_confidence():
    kept = filter_by_confidence(sample_detections(), threshold=0.5)
    labels = [d["label"] for d in kept]
    assert labels == ["person", "helmet"]


def test_filter_boundary_is_inclusive():
    """A detection exactly at the threshold should be kept (>=)."""
    dets = [make_detection("edge", 0.50, {"x1": 0, "y1": 0, "x2": 1, "y2": 1})]
    assert len(filter_by_confidence(dets, threshold=0.50)) == 1


def test_filter_threshold_zero_keeps_all():
    assert len(filter_by_confidence(sample_detections(), threshold=0.0)) == 4


def test_filter_threshold_one_keeps_only_perfect():
    assert filter_by_confidence(sample_detections(), threshold=1.0) == []


def test_filter_empty_input():
    assert filter_by_confidence([], threshold=0.5) == []


def test_filter_rejects_out_of_range_threshold():
    with pytest.raises(ValueError):
        filter_by_confidence(sample_detections(), threshold=1.5)


# ── make_detection validation ─────────────────────────────────────────────────

def test_make_detection_rejects_bad_confidence():
    with pytest.raises(ValueError):
        make_detection("x", 1.2, {"x1": 0, "y1": 0, "x2": 1, "y2": 1})


# ── top_detection ─────────────────────────────────────────────────────────────

def test_top_detection_returns_most_confident():
    assert top_detection(sample_detections())["label"] == "person"


def test_top_detection_empty_returns_none():
    assert top_detection([]) is None
