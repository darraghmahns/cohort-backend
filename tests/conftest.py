import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine, Base

@pytest.fixture(scope="function")
def client():
    # Create the database tables before running the tests
    Base.metadata.create_all(bind=engine)
    client = TestClient(app)
    yield client
    # Drop the tables after the tests
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()