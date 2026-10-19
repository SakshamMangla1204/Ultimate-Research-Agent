export interface ResearchRecord { id: string; title: string; query: string; at: string; status: 'completed' | 'failed' | 'running' | 'waiting' | 'unknown'; duration?: number; report?: string; sources: Array<{ title: string; url: string; domain?: string; id?: string }>; errors: string[]; }
export interface Preferences { theme: 'dark' | 'light'; }
const HISTORY = 'flux.history.v1';
const SAVED = 'flux.saved-reports.v1';
const PREFS = 'flux.preferences.v1';
function read<T>(key: string, fallback: T): T { try { const value = localStorage.getItem(key); return value ? JSON.parse(value) as T : fallback; } catch { return fallback; } }
function write(key: string, value: unknown) { try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch { return false; } }
export const historyStore = {
  list: () => read<ResearchRecord[]>(HISTORY, []),
  save: (record: ResearchRecord) => write(HISTORY, [record, ...historyStore.list().filter(item => item.id !== record.id)]),
  remove: (id: string) => write(HISTORY, historyStore.list().filter(item => item.id !== id)),
};
export const savedReportsStore = {
  list: () => read<ResearchRecord[]>(SAVED, []),
  save: (record: ResearchRecord) => write(SAVED, [record, ...savedReportsStore.list().filter(item => item.id !== record.id)]),
  remove: (id: string) => write(SAVED, savedReportsStore.list().filter(item => item.id !== id)),
};
export const preferencesStore = {
  get: () => read<Preferences>(PREFS, { theme: 'dark' }),
  set: (value: Preferences) => write(PREFS, value),
};
