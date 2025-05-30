import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Test Item", "image": "test.png", "user": 1}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["item"]["name"] == "Test Item"
    assert data["item"]["image"] == "test.png"