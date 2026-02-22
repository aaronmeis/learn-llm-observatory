# learn-llm-observatory

Real-time trace and risk monitoring for GenAI applications.

## Purpose
Observe + diagnose LLM behaviors, latency spikes, and policy violations.

## Infographic Prompt
> **Prompt:** Generate a professional infographic for 'LLM Observatory', a real-time monitoring tool for GenAI. Visualize the ingest-to-UI pipeline: Ingest traces -> Enrich with eval labels -> Aggregate -> Store -> UI Dashboard. Show a 'latency_spike' alert triggering a drilldown to a specific trace.

## MVP Scope
- **Must-have:** Trace ingestion API, Dashboard with p95 latency, Explorer for trace drilldown.
- **Nice-to-have:** Real-time anomaly alerts, ClickHouse for high-volume spans.

## Quickstart
```bash
docker compose up -d
npm install --prefix frontend && npm run dev --prefix frontend
```
