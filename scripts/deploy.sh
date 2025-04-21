#!/bin/bash

# Update package lists
sudo apt-get update

# Install Docker if not already installed
if ! command -v docker &> /dev/null; then
    sudo apt-get install -y docker.io
    sudo systemctl enable docker
    sudo systemctl start docker
    # Add current user to docker group
    sudo usermod -aG docker $USER
fi

# Install Docker Compose if not already installed
if ! command -v docker-compose &> /dev/null; then
    sudo apt-get install -y docker-compose
fi

# Create necessary directories
mkdir -p ~/app/backend
mkdir -p ~/app/frontend

# Create docker-compose.yml
cat > ~/app/docker-compose.yml << 'EOL'
version: '3'
services:
  backend:
    image: ${DOCKERHUB_USERNAME}/url-shortener-backend:latest
    ports:
      - "8000:8000"
    environment:
      - DOCKERHUB_USERNAME=${DOCKERHUB_USERNAME}
    restart: always

  frontend:
    image: ${DOCKERHUB_USERNAME}/url-shortener-frontend:latest
    ports:
      - "80:80"
    environment:
      - REACT_APP_API_URL=http://localhost:8000
    depends_on:
      - backend
    restart: always
EOL

# Create .env file
cat > ~/app/.env << EOL
DOCKERHUB_USERNAME=${DOCKERHUB_USERNAME}
DOCKERHUB_TOKEN=${DOCKERHUB_TOKEN}
EOL

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Login to Docker Hub
echo "${DOCKERHUB_TOKEN}" | docker login -u "${DOCKERHUB_USERNAME}" --password-stdin

# Pull the latest images
docker-compose -f ~/app/docker-compose.yml pull

# Stop and remove existing containers
docker-compose -f ~/app/docker-compose.yml down

# Start the services
docker-compose -f ~/app/docker-compose.yml up -d 