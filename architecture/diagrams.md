# Architecture Diagrams - learn-llm-observatory

## System Pipeline

```mermaid
flowchart TD
  IN[Ingest\nTraces/Events from data-kit]
    --> N[Normalize\nparse fields, standardize IDs]
    --> E[Enrich\nroute/model_version/tool_name\nattach eval labels]
    --> A[Aggregate\nrollups by time + dimensions]
    --> ST[(Storage\nPostgres rollups\nClickHouse optional events)]
    --> UI[React SPA\nDashboard → Explorer → Drilldown]
```

## UI Screen Flow

```mermaid
flowchart LR
  A1[Dashboard\nKPIs + Alerts + Trends] --> A2[Trace Explorer\nFilters + Facets + Table]
  A2 --> A3[Trace Drilldown\nTimeline + Tags + Evidence]
  A3 -->|Open Case| C[Create/Link Case\n(agentic-investigator)]
```

## Scenario-to-UI Expectations

```mermaid
flowchart TD
  subgraph Scenario1[latency_spike]
    S1[latency_spike data]
    S1 --> D1[Dashboard change:\np95 ↑, timeouts ↑,\nTop route highlighted]
    D1 --> E1[Explorer:\nfilter route/time\nsee slow exemplars]
    E1 --> X1[Drilldown:\nspan timeline shows\nslow LLM or tool span]
  end

  subgraph Scenario2[tool_failure_storm]
    S2[tool_failure_storm data]
    S2 --> D2[Dashboard change:\ntool failure rate ↑,\nretry_count ↑]
    D2 --> E2[Explorer:\nfilter tool_name/status\nsee timeout exemplars]
    E2 --> X2[Drilldown:\nretries + tool timeouts\ncascade to latency]
  end
```
