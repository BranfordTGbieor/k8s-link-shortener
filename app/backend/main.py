from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import string
import random
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage (replace with database in production)
url_store: Dict[str, str] = {}

class URLRequest(BaseModel):
    url: str

def generate_short_code(length: int = 6) -> str:
    """Generate a random short code for the URL."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.post("/shorten")
async def shorten_url(request: URLRequest):
    """Shorten a URL and return the shortened version."""
    short_code = generate_short_code()
    url_store[short_code] = request.url
    return {"short_url": f"http://localhost:8000/{short_code}"}

@app.get("/{short_code}")
async def redirect_url(short_code: str):
    """Redirect to the original URL using the short code."""
    if short_code not in url_store:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"url": url_store[short_code]}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"} 