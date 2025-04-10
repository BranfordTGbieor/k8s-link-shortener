from fastapi.testclient import TestClient
from main import app
import pytest
import os

# Set testing environment
os.environ["TESTING"] = "true"

client = TestClient(app)

def test_shorten_url():
    response = client.post(
        "/shorten",
        json={"url": "https://example.com"}
    )
    assert response.status_code == 200
    assert "short_url" in response.json()

def test_redirect_url():
    # Test with the predefined test code
    response = client.get("/test123")
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