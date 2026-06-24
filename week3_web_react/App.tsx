// Week 3 — Web Basics & React Thinking
// Lab: a three-stage pipeline dashboard (Input -> Detection -> Output).
//
// Each stage card reflects its status with colour. The "Advance" button steps the pipeline
// one stage at a time (waiting -> running -> complete), reflecting the sequential pipeline.
// "Reset" returns all stages to waiting.
//
// Drop this file into a Vite + React + TS project's src/ folder (alongside types.ts) and
// render <App /> from main.tsx.

import { useState } from 'react';
import {
  Stage,
  StageStatus,
  initialStages,
  STATUS_COLOURS,
} from './types';

function StageCard({ stage }: { stage: Stage }) {
  return (
    <div
      style={{
        background: STATUS_COLOURS[stage.status],
        color: 'white',
        padding: 24,
        borderRadius: 8,
        minWidth: 140,
        textAlign: 'center',
      }}
    >
      <h3 style={{ margin: '0 0 8px' }}>{stage.label}</h3>
      <p style={{ margin: 0, fontWeight: 600 }}>{stage.status.toUpperCase()}</p>
    </div>
  );
}

export default function App() {
  const [stages, setStages] = useState<Stage[]>(initialStages);

  function advancePipeline() {
    setStages((prev) => {
      const next = prev.map((s) => ({ ...s })); // copy — never mutate state in place
      const running = next.findIndex((s) => s.status === 'running');
      if (running !== -1) {
        next[running].status = 'complete';
        if (running + 1 < next.length) next[running + 1].status = 'running';
      } else {
        const first = next.findIndex((s) => s.status === 'waiting');
        if (first !== -1) next[first].status = 'running';
      }
      return next;
    });
  }

  function reset() {
    setStages(initialStages.map((s) => ({ ...s, status: 'waiting' as StageStatus })));
  }

  const allComplete = stages.every((s) => s.status === 'complete');

  return (
    <main style={{ fontFamily: 'system-ui, sans-serif', padding: 32 }}>
      <h1>Uni_Vision — Pipeline Dashboard</h1>
      <div style={{ display: 'flex', gap: 16, margin: '24px 0' }}>
        {stages.map((stage) => (
          <StageCard key={stage.id} stage={stage} />
        ))}
      </div>
      <button onClick={advancePipeline} disabled={allComplete}>
        Advance
      </button>{' '}
      <button onClick={reset}>Reset</button>
      {allComplete && <p>Pipeline complete ✅</p>}
    </main>
  );
}
