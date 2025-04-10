from fastapi.testclient import TestClient
from main import create_app
import pytest
import os

# Set testing environment
os.environ["TESTING"] = "true"

@pytest.fixture
def test_store():
    return {}

@pytest.fixture
def client(test_store):
    app = create_app(test_store)
    return TestClient(app)

def test_shorten_url(client, test_store):
    response = client.post(
        "/shorten",
        json={"url": "https://example.com/"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "short_url" in data
    short_code = data["short_url"].split("/")[-1]
    assert test_store[short_code] == "https://example.com"  # Note: no trailing slash

def test_redirect_url(client, test_store):
    # First create a short URL
    response = client.post(
        "/shorten",
        json={"url": "https://example.com"}
    )
    assert response.status_code == 200
    data = response.json()
    short_code = data["short_url"].split("/")[-1]
    
    # Then test the redirect
    response = client.get(f"/{short_code}", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["Location"] == "https://example.com"

def test_invalid_url(client):
    response = client.post(
        "/shorten",
        json={"url": "not-a-url"}
    )
    assert response.status_code == 422

def test_nonexistent_code(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404 