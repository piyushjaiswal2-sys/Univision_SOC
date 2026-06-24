# Variables, Loops, Events, and Conditions

> One-page explanation in my own words, grounded in the Uni_Vision vision-pipeline idea.

A computer system is not magic and it is not one big brain. It is a set of small, predictable
steps arranged in an order. Before touching any AI, the four ideas below are enough to describe
how a camera-alert system behaves.

## Variable
A **variable** is a named box that stores a value the system needs to remember *right now*.
In a vision pipeline, `confidence_threshold = 0.5` is a variable: it holds the cut-off we use to
decide whether a detection is trustworthy. The name matters more than the value — `frame_count`,
`last_alert_time`, and `current_status` all describe *what* is being remembered. Change the value
in the box and the rest of the system behaves differently without rewriting any logic.

## Condition
A **condition** chooses between paths. It asks a yes/no question and the system goes one way or
the other. "**If** motion is detected, capture a frame; **otherwise** keep waiting." A condition is
how a system makes a decision instead of blindly doing the same thing every time. In Uni_Vision,
almost every useful behaviour is a condition: *if confidence is above the threshold, keep the
detection; else discard it.*

## Loop
A **loop** repeats a step. A camera does not look once — it looks again and again, frame after
frame, forever (or until told to stop). "**Repeat:** grab the next frame, check it, then grab the
next frame." Loops are why a system can run continuously. Without a loop, the program would
analyse a single image and exit.

## Event
An **event** is something that *happens* and triggers behaviour — a key press, a new frame
arriving, motion crossing a line, a button click on the dashboard. Events are what connect the
outside world to the system's logic. "**When** motion is detected → run the alert steps." Event-driven
thinking is exactly the Scratch model (`when green flag clicked`, `when key pressed`) and it is also
how the live dashboard updates: an event arrives, and the matching part of the system reacts.

## How they fit together (the pipeline)
These four primitives compose into a pipeline:

```
data enters  →  a function transforms it  →  a condition checks the result
             →  the next function receives it  →  the final output is shown or stored
```

A camera-alert system is just: a **loop** that runs forever, watching for an **event** (motion),
using **variables** to remember thresholds and counts, and using **conditions** to decide whether
to raise an alert. Everything more advanced — object detection, OCR, agents — is built on top of
exactly these ideas.

**One-line takeaway:** *systems are made of small logical steps, and variables / conditions /
loops / events are the four bricks every step is built from.*
