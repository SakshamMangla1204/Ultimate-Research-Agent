# flux.ai frontend

## Run locally

```sh
cd ultimate-research-agent/frontend
npm install
npm run dev
```

Vite serves the app at <http://localhost:5173> by default. This project includes a local `.env` pointing to the backend at `http://localhost:8000`. For a production bundle, run `npm run build`; `npm run preview` serves that bundle locally.

In a second terminal, from the `ultimate-research-agent` project directory, start the API:

```sh
python3 -m pip install -r requirements.txt
python3 -m uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

Set the selected provider key (currently `GOOGLE_API_KEY`, because `DEFAULT_MODEL` is `gemini`) and `TAVILY_API_KEY` in the backend environment or its root `.env` before submitting a research query. The health endpoint works without provider keys; research needs them.

## Backend connection

The frontend calls `GET /health` and `POST /research`; these routes are provided by `api.py`. No model-provider or search keys belong in frontend environment variables.

History, saved reports, and theme preference are stored in the browser's local storage.
