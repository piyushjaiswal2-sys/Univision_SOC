# Week 2 : Python As A Tool

**Focus:** functions, lists, dictionaries, and tests.

## Lab detection dictionaries + confidence filter
`detections.py` models a single detection as a dictionary `{label, confidence, box}` and provides:
- `make_detection(...)` — build one detection, validating confidence ∈ [0, 1].
- `average_confidence(scores)` — mean of a list of scores (0.0 for an empty list).
- `filter_by_confidence(detections, threshold)` the pipeline's "trust gate": drop low-confidence guesses.
- `top_detection(detections)` — the single most confident detection.

```bash
python detections.py
```

## Tests for threshold filtering
`test_detections.py` covers the boundary cases that matter: inclusive `>=` boundary, threshold 0
keeps all, threshold 1 keeps only perfect scores, empty input, and invalid threshold rejection.

```bash
pytest test_detections.py -v
```

## Why tests before complexity
Once detection feeds into preprocessing, OCR, tracking, and an API, a silent off-by-one in the
filter would corrupt everything downstream. Locking the behaviour with tests now means later
changes can be made with confidence debugging by observation is a skill, not a fallback.
