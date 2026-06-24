# Week 1 Lab — Camera Alert Flowchart

A flowchart for a motion-triggered camera alert. The rule taught in Week 1:
*"if motion is detected, capture a frame; otherwise keep waiting."*

This is the **event-driven loop** that the whole Uni_Vision pipeline later sits on top of.

## Flowchart (Mermaid)

```mermaid
flowchart TD
    A([Start camera]) --> B[Read next frame]
    B --> C{Motion detected?}
    C -- No --> B
    C -- Yes --> D[Capture / save frame]
    D --> E[Run quick check<br/>e.g. confidence threshold]
    E --> F{Above threshold?}
    F -- No --> G[Log as low-confidence<br/>no alert] --> B
    F -- Yes --> H[Raise ALERT<br/>attach evidence: frame + time + score]
    H --> I[(Store result & metrics)]
    I --> B
    B --> J{Stop requested?}
    J -- Yes --> K([Shutdown])
```

## Plain-text version (for graders who can't render Mermaid)

```
START
  |
  v
READ NEXT FRAME  <-------------------+
  |                                  |
  v                                  |
[ Motion detected? ] --No----------->+
  | Yes                              |
  v                                  |
CAPTURE / SAVE FRAME                 |
  |                                  |
  v                                  |
RUN QUICK CHECK (threshold)          |
  |                                  |
  v                                  |
[ Above threshold? ] --No--> LOG ----+
  | Yes                              |
  v                                  |
RAISE ALERT (frame + time + score)   |
  |                                  |
  v                                  |
STORE RESULT & METRICS --------------+
```

## Why this shape
- The **loop** back to *Read next frame* is what keeps the camera live.
- *Motion detected?* and *Above threshold?* are **conditions** — the two decisions the system makes.
- The arriving frame / motion crossing the line is the **event** that drives everything.
- `confidence threshold` and `last_alert_time` are the **variables** the system remembers.
- Every alert carries **evidence** (frame + time + confidence). Provenance is taught early in
  Uni_Vision: *every AI output should have evidence, time, source, and confidence.*
