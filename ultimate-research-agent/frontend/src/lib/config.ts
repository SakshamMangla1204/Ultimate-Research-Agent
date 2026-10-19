/**
 * flux.ai - Build-time / runtime configuration.
 *
 * Everything here is read from environment variables at load time. The only
 * value the developer is expected to set is VITE_API_URL; the rest fall
 * back to sensible defaults so the app still renders in a disconnected state.
 */

export interface Config {
  apiUrl: string;
  /** Derived base path used for constructing API routes. */
  apiBase: string;
  /** True when no API URL has been configured (demo / offline mode). */
  isDisconnected: boolean;
}

function readEnv(name: string, fallback = ''): string {
  // In a Vite app, `import.meta.env` exposes Vite-served environment
  // variables. Variables must start with VITE_ to be exposed to client code.
  const client = (import.meta as any)?.env?.VITE_API_URL;
  // During SSR / tests, import.meta.env is undefined; fall back to
  // @ts-ignore - process is provided by @types/node
  const nodeEnv = typeof process !== 'undefined' ? process.env : undefined;
  return (client ?? (nodeEnv ? nodeEnv[name] : undefined) ?? fallback);
}

export const config: Config = {
  apiUrl: readEnv('VITE_API_URL', ''),
  apiBase: readEnv('VITE_API_BASE', ''),
  isDisconnected: readEnv('VITE_API_URL', '').trim() === '',
};

/**
 * Convenience flag. Returns true when the frontend is running without a
 * configured backend (for example, when VITE_API_URL is empty). The UI can
 * use this to show honest "backend is disconnected" states.
 */
export function isDisconnected(): boolean {
  return config.isDisconnected;
}
