from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
import string
import random
from pydantic import BaseModel, HttpUrl
from typing import Dict
from urllib.parse import urlparse, urlunparse

# Default store for production
default_store: Dict[str, str] = {}

def normalize_url(url: str) -> str:
    """Normalize URL by removing trailing slash."""
    parsed = urlparse(url)
    # Remove trailing slash from path
    path = parsed.path.rstrip('/')
    # Reconstruct URL without trailing slash
    return urlunparse(parsed._replace(path=path))

def create_app(store: Dict[str, str] = None):
    app = FastAPI()

    # Use provided store or default
    url_store = store if store is not None else default_store.copy()  # Create a copy to avoid sharing

    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    class URLRequest(BaseModel):
        url: HttpUrl  # This will automatically validate URLs

    def generate_short_code(length: int = 6) -> str:
        """Generate a random short code for the URL."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    @app.post("/shorten")
    async def shorten_url(request: URLRequest):
        """Shorten a URL and return the shortened version."""
        nonlocal url_store  # Use the closure variable
        short_code = generate_short_code()
        normalized_url = normalize_url(str(request.url))
        url_store[short_code] = normalized_url
        return {"short_url": f"http://localhost:8000/{short_code}"}

    @app.get("/{short_code}")
    async def redirect_url(short_code: str):
        """Redirect to the original URL using the short code."""
        nonlocal url_store  # Use the closure variable
        if short_code not in url_store:
            raise HTTPException(status_code=404, detail="URL not found")
        return Response(
            status_code=307,
            headers={"Location": url_store[short_code]}
        )

    @app.get("/health")
    async def health_check():
        """Health check endpoint."""
        return {"status": "healthy"}

    return app

# Create the default app instance
app = create_app() 