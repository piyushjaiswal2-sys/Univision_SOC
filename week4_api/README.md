# Week 4 : APIs & JSON Contracts

**Focus:** routes, JSON, validation, status codes (FastAPI + Pydantic).

## Image-analysis API contract
`main.py` defines three routes:

| Method | Route | Purpose |
|--------|-------|---------|
| GET | `/health` | API status + version (monitoring) |
| POST | `/analyse` | Accept image URL + config, return detections |
| GET | `/results/{id}` | Retrieve a stored result by id |

Request/response shapes are enforced by Pydantic models, so invalid input is rejected with a
422 automatically and the interactive docs are generated for free.

## Homework
Worked request/response bodies (success + error) and the required-vs-optional field table are in
[`examples.md`](examples.md).

## Run it
```bash
pip install "fastapi[standard]" uvicorn
uvicorn main:app --reload
# open http://127.0.0.1:8000/docs  (interactive Swagger UI)
# or http://127.0.0.1:8000/health
```

Try a request:
```bash
curl -X POST http://127.0.0.1:8000/analyse \
  -H "Content-Type: application/json" \
  -d '{"image_url":"https://example.com/f.jpg","confidence_threshold":0.6}'
```

## Key lesson
Write the contract *before* the implementation. A clear contract prevents confused systems later.
