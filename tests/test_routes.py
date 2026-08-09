from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_endpoint() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI E-Commerce is running!"}


def test_home_endpoint() -> None:
    response = client.get("/api/v1/home/")

    assert response.status_code == 200
    assert response.json() == {"message": "World"}
