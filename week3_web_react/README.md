# Week 3 — Web Basics & React Thinking

**Focus:** HTML structure, CSS appearance, JS behaviour, TypeScript types, React state.

## Lab — three-stage dashboard mock
- `types.ts` — `StageStatus`, `Stage`, `PipelineEvent` types, the initial stage list, and a
  status→colour map.
- `App.tsx` — a dashboard showing **Input → Detection → Output**. Each card colours itself by
  status (grey/blue/green/red). **Advance** steps one stage at a time; **Reset** clears it.

## Homework — UI state diagram

| From | To | Trigger |
|------|----|---------|
| `idle` | `stage_running` | User clicks **Advance** — first stage becomes *running* |
| `stage_running` | `stage_running` | Stage completes — next stage becomes *running* |
| `stage_running` | `pipeline_complete` | Last stage completes — all stages *complete* |
| `stage_running` | `error_state` | Stage throws — its card turns red, pipeline halts |
| `pipeline_complete` | `idle` | User clicks **Reset** — all stages back to *waiting* |
| `error_state` | `idle` | User clicks **Retry** — state resets to *waiting* |

## Why a dashboard needs state
A dashboard is a *live view of a changing system*, not a static page. **State** is the data the
component remembers between events. Without it, clicking a button would have no lasting effect.
Separating state from display (the React model) makes it easy to add stages or change logic
without redesigning the page.

## How to run
```bash
npm create vite@latest univision-dashboard -- --template react-ts
cd univision-dashboard
# copy App.tsx and types.ts into src/  (replace the generated App.tsx)
npm install
npm run dev
```
