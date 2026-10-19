/**
 * flux.ai - TypeScript types for the research workflow data model.
 *
 * These types describe the eventual LangGraph pipeline state and the
 * report returned by the backend. They are intentionally aligned with the
 * Python ResearchState schema so the frontend can display real backend
 * telemetry without inventing fields.
 */

export type AgentId = 'planner' | 'researcher' | 'analyst' | 'synthesizer';

export type AgentStatus = 'waiting' | 'running' | 'completed' | 'failed';

export interface AgentNode {
  id: AgentId;
  name: string;
  description: string;
  status: AgentStatus;
  /** RFC 3339 timestamp for when the stage entered / left a state. */
  timestamp?: string;
  /** Optional duration in seconds for completed stages. */
  duration?: number;
  /** Error message for failed stages. Plaintext, never raw stack traces. */
  error?: string;
  /** Raw detail available on expand; client must hide this for non-technical users. */
  detail?: string;
}

export interface Source {
  title: string;
  url: string;
  content: string;
  /** Optional domain derived by the backend. */
  domain?: string;
  /** Optional backend-provided identifier (e.g. Tavily result ID). */
  id?: string;
}

export interface ToolCall {
  tool: string;
  query: string;
}

export interface ToolResult {
  task: string;
  results: Array<{
    title: string;
    url: string;
    content: string;
  }>;
}

export interface ResearchRun {
  /** Backend-generated run identifier. */
  id: string;
  /** Original user query. */
  query: string;
  /** When the run started. */
  startedAt?: string;
  /** When the run ended. */
  completedAt?: string;
  /** Elapsed wall-clock time, when the backend reports it. */
  duration?: number;
  /** Aggregated per-agent telemetry. The backend decides what to populate */
  /** here; the frontend must never fabricate missing values. */
  results: {
    planner?: AgentNode;
    researcher?: AgentNode;
    analyst?: AgentNode;
    synthesizer?: AgentNode;
  };
  /** Aggregated probe status rather than per-agent telemetry. */
  probeStatus: string | null;
  sources: Source[];
  /** Plaintext notes for the user, never stack traces. */
  notes: string;
  /** Final report content rendered from Markdown. */
  report: string;
  /** Errors encountered during the run, if any. */
  errors: string[];
}

/** Fields that a research run accepts from the caller. */
export interface ResearchInput {
  query: string;
  goal?: string;
  research_type?: string;
  constraints?: Record<string, any>;
  output_requirements?: Record<string, any>;
}

/**
 * When a run completes, the backend may return one of these shapes.
 * The frontend normalizes whatever it receives; if the response does not
 * carry a report, the UI shows an honest "no report returned" state.
 */
export type RunResponse =
  | { ok: true; run: ResearchRun }
  | { ok: false; error: string; status: number };