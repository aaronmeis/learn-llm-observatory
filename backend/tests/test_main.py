from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_ingest():
    response = client.post("/ingest", json={"id": "trace-123"})
    assert response.status_code == 200
    assert response.json()["status"] == "accepted"
