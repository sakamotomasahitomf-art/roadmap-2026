from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_tasks_crud():
    # create
    r = client.post("/api/v1/tasks", json={"title": "T1"})
    assert r.status_code == 201
    tid = r.json()["id"]

    # list
    r = client.get("/api/v1/tasks")
    assert r.status_code == 200
    assert any(t["id"] == tid for t in r.json())

    # get
    r = client.get(f"/api/v1/tasks/{tid}")
    assert r.status_code == 200

    # delete
    r = client.delete(f"/api/v1/tasks/{tid}")
    assert r.status_code == 204
