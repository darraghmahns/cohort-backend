import pytest
from app import schemas
# from app.crud import get_user_by_email
from app.database import Base, engine  # Import the Base and engine to drop tables

def test_create_user(client):
    response = client.post("/users/", json={"email": "user@example.com", "password": "password123"})
    assert response.status_code == 200
    assert "id" in response.json()

def test_create_user_duplicate_email(client):
    client.post("/users/", json={"email": "user@example.com", "password": "password123"})
    response = client.post("/users/", json={"email": "user@example.com", "password": "password123"})
    assert response.status_code == 400

def test_read_user(client):
    response = client.post("/users/", json={"email": "user@example.com", "password": "password123"})
    user_id = response.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == "user@example.com"

def test_delete_user(client):
    response = client.post("/users/", json={"email": "delete_me@example.com", "password": "password123"})
    assert response.status_code == 200
    user_id = response.json()["id"]

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404

    # Drop the tables after this specific test
    from app.database import Base, engine
    Base.metadata.drop_all(bind=engine)