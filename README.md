# 🔗 Kubernetes URL Shortener

A real-world, production-like URL Shortener application deployed and managed using Kubernetes. This project is designed to reinforce and showcase Certified Kubernetes Application Developer (CKAD) concepts through hands-on implementation.

---

## 📌 Project Goals

- Deploy a full-stack URL shortener application on Kubernetes.
- Practice all core CKAD skills: Deployments, Services, ConfigMaps, Secrets, Probes, Persistent Storage, Networking, RBAC, and Autoscaling.
- Build a robust, observable, and scalable system.
- Showcase Kubernetes manifest authoring skills in a real-world scenario.

---

## 🚀 Tech Stack

### 🔧 Core
- **Kubernetes (k8s)** — container orchestration
- **kubectl** — k8s CLI
- **Docker** — container build & management
- **Kustomize** — configuration customization (optional)

### 🧠 Application Stack
- **Frontend**: React (or static HTML + JS if you want to focus purely on backend)
- **Backend**: FastAPI / Flask / Express.js (choose based on language preference)
- **Database**: PostgreSQL (stateful workload)

### 📈 Observability
- **Prometheus** — metrics collection
- **Grafana** — metrics visualization
- **liveness/readiness probes** — app health checks

---

## 📋 Prerequisites

- Kubernetes cluster (minikube, kind, or cloud-based)
- kubectl configured to access your cluster
- Docker installed and running
- Helm (for package management)
- Git

---

## 📂 Directory Structure

```
k8s-url-shortener/
├── .github/                    # GitHub Actions workflows
│   └── workflows/
│       ├── ci.yml             # Continuous Integration
│       └── cd.yml             # Continuous Deployment
├── app/                       # Application code
│   ├── frontend/             # React frontend
│   │   ├── src/
│   │   ├── public/
│   │   └── Dockerfile
│   └── backend/              # FastAPI/Flask/Express backend
│       ├── src/
│       ├── tests/
│       └── Dockerfile
├── k8s/                      # Kubernetes manifests
│   ├── base/                 # Base Kustomize configurations
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── kustomization.yaml
│   ├── overlays/             # Environment-specific configurations
│   │   ├── dev/
│   │   └── prod/
│   ├── monitoring/           # Monitoring stack manifests
│   │   ├── prometheus/
│   │   └── grafana/
│   └── storage/             # Persistent storage configurations
├── scripts/                  # Utility scripts
│   ├── deploy.sh
│   └── test.sh
├── docs/                    # Documentation
│   ├── architecture.md
│   └── api.md
├── .gitignore
├── README.md
└── Makefile                 # Common commands
```

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/k8s-url-shortener.git
   cd k8s-url-shortener
   ```

2. **Build and push Docker images**
   ```bash
   make build
   make push
   ```

3. **Deploy to Kubernetes**
   ```bash
   make deploy
   ```

4. **Access the application**
   ```bash
   kubectl port-forward service/url-shortener-frontend 8080:80
   ```
   Visit http://localhost:8080

---

## 🔍 Monitoring and Observability

The application includes:
- Prometheus for metrics collection
- Grafana dashboards for visualization
- Built-in health checks
- Logging and tracing capabilities

To access monitoring:
```bash
kubectl port-forward service/prometheus 9090:9090
kubectl port-forward service/grafana 3000:3000
```

---

## 📊 Scaling and Performance

- Horizontal Pod Autoscaling (HPA) configured
- Resource limits and requests defined
- Database connection pooling
- Caching layer for frequently accessed URLs

---

## 🔒 Security

- RBAC configurations
- Network policies
- Secrets management
- TLS termination
- Regular security updates

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Kubernetes community
- CNCF projects
- Open source contributors

