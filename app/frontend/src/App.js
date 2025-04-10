import React, { useState } from 'react';
import './App.css';

function App() {
  const [url, setUrl] = useState('');
  const [shortUrl, setShortUrl] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/shorten', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });
      const data = await response.json();
      setShortUrl(data.short_url);
      setError('');
    } catch (err) {
      setError('Failed to shorten URL');
      setShortUrl('');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>K8s Link Shortener</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter URL to shorten"
            required
          />
          <button type="submit">Shorten</button>
        </form>
        {shortUrl && (
          <div className="result">
            <p>Short URL:</p>
            <a href={shortUrl} target="_blank" rel="noopener noreferrer">
              {shortUrl}
            </a>
          </div>
        )}
        {error && <p className="error">{error}</p>}
      </header>
    </div>
  );
}

export default App; 