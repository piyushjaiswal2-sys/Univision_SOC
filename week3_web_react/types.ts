// Week 3 — Web Basics & React Thinking
// TypeScript type definitions for the three-stage pipeline dashboard.

export type StageStatus = 'waiting' | 'running' | 'complete' | 'error';

export interface Stage {
  id: string;
  label: string;
  status: StageStatus;
}

// A single live event streamed from the pipeline (used in the homework state diagram
// and again in Week 10 when the events arrive over a WebSocket).
export interface PipelineEvent {
  stageId: string;
  status: StageStatus;
  timestamp: string; // ISO-8601
  message?: string;
}

export const initialStages: Stage[] = [
  { id: 'input', label: 'Input', status: 'waiting' },
  { id: 'detection', label: 'Detection', status: 'waiting' },
  { id: 'output', label: 'Output', status: 'waiting' },
];

export const STATUS_COLOURS: Record<StageStatus, string> = {
  waiting: '#94a3b8', // grey
  running: '#3b82f6', // blue
  complete: '#22c55e', // green
  error: '#ef4444', // red
};
