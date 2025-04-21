# 🚀 Kubernetes URL Shortener

A modern, production-ready URL shortener application that demonstrates best practices in Kubernetes deployment and cloud-native development. This project showcases a full-stack application with a React frontend, FastAPI backend, and PostgreSQL database, all containerized and orchestrated using Kubernetes. The deployment is automated through GitHub Actions CI/CD pipeline, making it a perfect example of modern DevOps practices.

## 📋 Table of Contents
- [Features](#-features)
- [Architecture](#-architecture)
- [Logical Flow](#-logical-flow)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Getting Started](#-getting-started)
- [Development](#-development)
- [Deployment](#-deployment)
- [Cleanup](#-cleanup)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features
- 🔗 Shorten long URLs to memorable short codes with customizable expiration
- 🌐 Modern, responsive web interface built with React
- ⚡ FastAPI backend for high performance and automatic API documentation
- 🐳 Containerized with Docker for consistent environments
- ☸️ Kubernetes deployment with proper resource management
- 🔄 GitHub Actions CI/CD pipeline for automated testing and deployment
- 🔒 Secure with network policies and proper access controls
- 📊 Built-in monitoring and health checks
- 💰 Cost-optimized for demo purposes with t2.micro instances
- 🔐 Environment variable management and secrets handling
- 📈 Scalable architecture ready for production workloads

## 🏗️ Architecture
![Architecture Diagram](docs/architecture.png)

The application follows a microservices architecture with clear separation of concerns:
- **Frontend**: React-based single-page application
- **Backend**: FastAPI service handling URL shortening logic
- **Database**: PostgreSQL for persistent storage
- **Infrastructure**: AWS EKS cluster with Terraform provisioning
- **CI/CD**: GitHub Actions for automated deployment

## 🔄 Logical Flow
```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  Frontend       │────▶│  Backend        │────▶│  PostgreSQL     │
│  (React)        │     │  (FastAPI)      │     │  Database       │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## 📁 Project Structure
```
k8s-url-shortener/
├── .github/                    # GitHub Actions workflows
│   └── workflows/
│       └── ci.yml             # CI/CD pipeline configuration
├── app/                       # Application code
│   ├── frontend/             # React frontend
│   │   ├── src/
│   │   ├── public/
│   │   └── Dockerfile
│   └── backend/              # FastAPI backend
│       ├── src/
│       ├── tests/
│       └── Dockerfile
├── k8s/                      # Kubernetes manifests
│   ├── base/                 # Base configurations
│   │   ├── backend-deployment.yaml
│   │   ├── frontend-deployment.yaml
│   │   ├── service.yaml
│   │   └── kustomization.yaml
│   └── config/              # Additional configurations
├── terraform/               # Infrastructure as Code
│   ├── main.tf
│   ├── variables.tf
│   └── iam_policy.json
├── docs/                    # Documentation
│   └── architecture.png    # Architecture diagram
├── .env.example            # Environment variables template
├── .gitignore
└── README.md
```

## 📋 Prerequisites
- Docker and Docker Compose for containerization
- kubectl for Kubernetes cluster interaction
- AWS CLI for cloud resource management
- Terraform for infrastructure provisioning
- Python 3.8+ for backend development
- Node.js 14+ for frontend development
- Git for version control

## 🚀 Getting Started
1. Clone the repository:
```bash
git clone https://github.com/yourusername/k8s-url-shortener.git
cd k8s-url-shortener
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your values:
# - AWS credentials
# - Docker Hub credentials
# - Database configuration
```

3. Install dependencies:
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

## 💻 Development
1. Start the backend:
```bash
cd backend
uvicorn main:app --reload
```

2. Start the frontend:
```bash
cd frontend
npm start
```

## 🚀 Deployment
The application is deployed using GitHub Actions. The workflow:
1. 🧪 Runs tests for both frontend and backend
2. 🐳 Builds Docker images for all components
3. 📦 Pushes images to Docker Hub
4. ☸️ Deploys to EKS cluster
5. 🔍 Verifies deployment health
6. 🌐 Configures LoadBalancer for external access

To deploy manually:
```bash
# Apply Kubernetes manifests
kubectl apply -f k8s/base/

# Check deployment status
kubectl get pods
kubectl get services
```

## 🧹 Cleanup
To clean up resources:
1. Delete the LoadBalancer service:
```bash
kubectl delete service url-shortener-frontend
```

2. Run Terraform destroy:
```bash
cd terraform
terraform destroy -auto-approve
```

Note: If Terraform destroy fails due to LoadBalancer dependencies, you may need to manually delete the Classic Load Balancer in AWS Console or using AWS CLI.

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

