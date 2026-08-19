from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_create_user_success():
    payload = {
        "username": "vishwa",
        "email": "vishwa@archlinux.org"
    }
    
    response = client.post("/api/v1/users/", json=payload)
    
    # 1. Verify HTTP status
    assert response.status_code == 200
    
    # 2. Verify data contract
    data = response.json()
    assert data["username"] == "vishwa"
    assert data["email"] == "vishwa@archlinux.org"
    assert "id" in data  # Ensure our service generated the ID