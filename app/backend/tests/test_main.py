from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_shorten_url():
    response = client.post(
        "/shorten",
        json={"url": "https://example.com"}
    )
    assert response.status_code == 200
    assert "short_url" in response.json()

def test_redirect_url():
    # First create a short URL
    response = client.post(
        "/shorten",
        json={"url": "https://example.com"}
    )
    short_url = response.json()["short_url"]
    code = short_url.split("/")[-1]

    # Then test the redirect
    response = client.get(f"/{code}")
    assert response.status_code == 307  # Temporary redirect
    assert response.headers["location"] == "https://example.com"

def test_invalid_url():
    response = client.post(
        "/shorten",
        json={"url": "not-a-url"}
    )
    assert response.status_code == 422  # Validation error

def test_nonexistent_code():
    response = client.get("/nonexistent")
    assert response.status_code == 404 