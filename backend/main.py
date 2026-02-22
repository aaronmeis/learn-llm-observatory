from fastapi import FastAPI

app = FastAPI(title="LLM Observatory API")

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/ingest")
async def ingest_trace(trace: dict):
    return {"status": "accepted", "trace_id": trace.get("id", "unknown")}
