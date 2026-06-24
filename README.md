# Uni_Vision — SOC Midterm Submission (Weeks 1–6)

A real-time visual-intelligence learning project built as part of the **Uni_Vision Concept Learning Curriculum** (Seasons of Code).

Uni_Vision is taught as a *layered system*, not a single model. The prototype accepts images / video / camera streams, processes them through configurable workflow blocks, detects objects/text/anomalies, streams progress to a dashboard, and can use agentic AI tools to inspect and explain the system.

> **This repository covers the midterm portion: Weeks 1 through 6.**

---

## What's inside

| Week | Topic | Folder | Key deliverable |
|------|-------|--------|-----------------|
| 1 | Computing Without Fear | [`week1_foundations/`](week1_foundations) | Concepts write-up + camera-alert flowchart |
| 2 | Python As A Tool | [`week2_python/`](week2_python) | Detection dictionaries + confidence filter + tests |
| 3 | Web Basics & React Thinking | [`week3_web_react/`](week3_web_react) | Three-stage pipeline dashboard (React + TS) |
| 4 | APIs & JSON Contracts | [`week4_api/`](week4_api) | FastAPI image-analysis API contract |
| 5 | Blocks & Graphs | [`week5_blocks_graphs/`](week5_blocks_graphs) | Block-graph validation + topological sort |
| 6 | Images As Arrays | [`week6_images/`](week6_images) | OpenCV load / inspect / resize / grayscale / crop |

The full written submission is in [`docs/UniVision_SOC_Midterm_Weeks1-6.docx`](docs).

---

## Repository layout

```text
UniVision-SOC/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   └── UniVision_SOC_Midterm_Weeks1-6.docx
├── week1_foundations/
│   ├── README.md
│   ├── concepts.md
│   └── camera_alert_flowchart.md
├── week2_python/
│   ├── detections.py
│   ├── test_detections.py
│   └── README.md
├── week3_web_react/
│   ├── types.ts
│   ├── App.tsx
│   └── README.md
├── week4_api/
│   ├── main.py
│   ├── examples.md
│   └── README.md
├── week5_blocks_graphs/
│   ├── graph_validation.py
│   ├── test_graph_validation.py
│   └── README.md
└── week6_images/
    ├── image_basics.py
    └── README.md
```

---

## Quick start

```bash
# 1. Clone
git clone <your-repo-url>
cd UniVision-SOC

# 2. (Recommended) create a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt
```

### Run the Python deliverables

```bash
# Week 2 — detection filtering + tests
python week2_python/detections.py
pytest week2_python/test_detections.py -v

# Week 5 — block graph validation + topological sort
python week5_blocks_graphs/graph_validation.py
pytest week5_blocks_graphs/test_graph_validation.py -v

# Week 6 — image as arrays (auto-generates a sample image if none given)
python week6_images/image_basics.py
```

### Run the Week 4 API

```bash
pip install "fastapi[standard]" uvicorn
uvicorn week4_api.main:app --reload
# open http://127.0.0.1:8000/docs for the interactive Swagger UI
```

### Week 3 dashboard

The `week3_web_react/` files are reference React + TypeScript components. To run them inside a Vite + React + TS project, drop `App.tsx` / `types.ts` into `src/` and start the dev server. See that folder's README.

---

## Author

Piyush Jaiswal (Roll No. **24B2454**) — Seasons of Code (SOC), Uni_Vision Concept Learning Curriculum.
Mentors: **Sayandeep** and **Dhruv**.
