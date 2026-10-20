from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    assert len(response.json()["orders"]) == 2

def test_get_order():
    response = client.get("/orders/1")
    assert response.status_code == 200
    assert response.json()["item"] == "widget"
