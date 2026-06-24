# Worked Request & Response Bodies

Fully worked examples for every route, including success and error cases.

## `GET /health` : success
```json
{
  "status": "ok",
  "version": "0.1.0"
}
```

## `POST /analyse` : request body
```json
{
  "image_url": "https://example.com/frames/frame_00142.jpg",
  "model_name": "yolov8n",
  "confidence_threshold": 0.6,
  "max_detections": 5
}
```

## `POST /analyse` : success response
```json
{
  "result_id": "a3f2c1d0-7e44-4b8a-9c12-1e6b2f3a5d78",
  "image_url": "https://example.com/frames/frame_00142.jpg",
  "detections": [
    { "label": "person", "confidence": 0.92, "box": { "x1": 50, "y1": 30, "x2": 200, "y2": 380 } },
    { "label": "helmet", "confidence": 0.78, "box": { "x1": 70, "y1": 20, "x2": 160, "y2": 80 } }
  ],
  "processing_time_ms": 143.2,
  "created_at": "2025-09-14T10:22:04.331Z"
}
```

## `POST /analyse`: validation error (422)
If a required field is missing or a value is out of range, FastAPI/Pydantic returns 422 automatically:
```json
{
  "detail": [
    { "loc": ["body", "image_url"], "msg": "field required", "type": "value_error.missing" },
    { "loc": ["body", "confidence_threshold"], "msg": "ensure this value is less than or equal to 1.0", "type": "value_error.number.not_le" }
  ]
}
```

## `GET /results/{id}` : not found (404)
```json
{ "detail": "Result not found" }
```

## Required vs optional fields

| Field | Required? | Default | Constraint |
|-------|-----------|---------|------------|
| `image_url` | Yes | — | must be a valid URL |
| `model_name` | No | `"yolov8n"` | — |
| `confidence_threshold` | No | `0.5` | `0.0 ≤ x ≤ 1.0` |
| `max_detections` | No | `10` | `> 0` |

## Why API responses should be predictable
Another app (the Week 3 dashboard, an agent in Week 11) must know *exactly* what fields it will
receive. A predictable, validated contract means clients can be written before the server is
finished, and malformed input is rejected at the door instead of corrupting downstream logic.
