import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { act } from 'react';
import '@testing-library/jest-dom';
import App from './App';

describe('App Component', () => {
  beforeEach(() => {
    // Clear all mocks before each test
    jest.clearAllMocks();
  });

  test('renders the URL shortener form', () => {
    render(<App />);
    expect(screen.getByText('K8s Link Shortener')).toBeInTheDocument();
    expect(screen.getByPlaceholderText('Enter URL to shorten')).toBeInTheDocument();
    expect(screen.getByText('Shorten')).toBeInTheDocument();
  });

  test('handles URL shortening successfully', async () => {
    // Mock a successful API response
    global.fetch = jest.fn().mockImplementationOnce(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ short_url: 'http://localhost:8000/abc123' }),
      })
    );

    render(<App />);
    
    // Enter a URL
    const input = screen.getByPlaceholderText('Enter URL to shorten');
    await act(async () => {
      fireEvent.change(input, { target: { value: 'https://example.com' } });
    });
    
    // Submit the form
    const button = screen.getByText('Shorten');
    await act(async () => {
      fireEvent.click(button);
    });
    
    // Wait for the API call and check the result
    await waitFor(() => {
      expect(fetch).toHaveBeenCalledWith('http://localhost:8000/shorten', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: 'https://example.com' }),
      });
    });

    // Check that the short URL is displayed
    await waitFor(() => {
      expect(screen.getByText('http://localhost:8000/abc123')).toBeInTheDocument();
    });
  });

  test('handles API errors', async () => {
    // Mock a failed API response
    global.fetch = jest.fn().mockImplementationOnce(() =>
      Promise.resolve({
        ok: false,
        status: 422,
        json: () => Promise.resolve({ detail: 'Invalid URL' }),
      })
    );

    render(<App />);
    
    // Enter an invalid URL
    const input = screen.getByPlaceholderText('Enter URL to shorten');
    await act(async () => {
      fireEvent.change(input, { target: { value: 'not-a-url' } });
    });
    
    // Submit the form
    const button = screen.getByText('Shorten');
    await act(async () => {
      fireEvent.click(button);
    });
    
    // Wait for the error message
    await waitFor(() => {
      expect(screen.getByText('Invalid URL')).toBeInTheDocument();
    });
  });
}); 