import type { ResearchRun, ResearchInput } from '../types/research';

const apiUrl = () => (import.meta.env.VITE_API_URL ?? '').trim().replace(/\/$/, '');

export class ApiError extends Error {
  constructor(message: string, public status?: number) { super(message); this.name = 'ApiError'; }
}

async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const base = apiUrl();
  if (!base) throw new ApiError('No backend URL is configured. Set VITE_API_URL in frontend/.env to connect a FastAPI service.');
  const controller = new AbortController();
  // Research invokes the full graph and web search, so allow a longer window.
  const timer = window.setTimeout(() => controller.abort(), path === '/research' ? 300_000 : 30_000);
  try {
    const response = await fetch(`${base}${path}`, { ...init, signal: controller.signal, headers: { Accept: 'application/json', ...(init.body ? { 'Content-Type': 'application/json' } : {}), ...init.headers } });
    if (!response.ok) {
      let message = `Backend returned HTTP ${response.status}.`;
      try {
        const body = await response.json() as { detail?: unknown; error?: unknown };
        if (typeof body.detail === 'string') message = body.detail;
        else if (typeof body.error === 'string') message = body.error;
      } catch { /* use the status-based message */ }
      throw new ApiError(message, response.status);
    }
    try { return await response.json() as T; } catch { throw new ApiError('Backend response was not valid JSON.', response.status); }
  } catch (error) {
    if (error instanceof ApiError) throw error;
    if (error instanceof DOMException && error.name === 'AbortError') throw new ApiError('The backend request timed out.');
    throw new ApiError('Could not reach the backend. Check that it is running and that the API URL is correct.');
  } finally { window.clearTimeout(timer); }
}

export function isBackendConfigured(): boolean { return Boolean(apiUrl()); }
export async function health(): Promise<boolean> {
  if (!apiUrl()) return false;
  try { await request('/health', { signal: AbortSignal.timeout(8_000) }); return true; } catch { return false; }
}

/** Proposed integration contract. These routes do not exist in the current Python CLI project. */
export async function research(input: ResearchInput): Promise<ResearchRun> {
  const data = await request<unknown>('/research', { method: 'POST', body: JSON.stringify({ query: input.query }) });
  if (!data || typeof data !== 'object') throw new ApiError('The backend did not return a research result.');
  const value = data as Record<string, unknown>;
  if (typeof value.report !== 'string' && typeof value.final_report !== 'string') throw new ApiError('The backend response did not contain a report.');
  const report = String(value.report ?? value.final_report);
  return { id: String(value.id ?? value.run_id ?? crypto.randomUUID()), query: input.query, report, sources: Array.isArray(value.sources) ? value.sources as ResearchRun['sources'] : [], results: {}, probeStatus: null, notes: '', errors: [], startedAt: typeof value.started_at === 'string' ? value.started_at : undefined, completedAt: typeof value.completed_at === 'string' ? value.completed_at : undefined };
}
