# Fluid AI DevOps Challenge

## Architecture

GitHub
↓
GitHub Actions (CI)
↓
Docker Image
↓
Kind Kubernetes Cluster

├── Flask Deployment
│   └── Flask Service
│
└── MongoDB Deployment
    └── MongoDB Service

## Components

- Flask Backend
- MongoDB Database
- Docker Containerization
- Kubernetes Deployments & Services
- GitHub Actions CI Pipeline
- Readiness Probe
- Liveness Probe

## Reliability Improvement

Implemented:
- Readiness Probe
- Liveness Probe

Benefits:
- Prevents traffic to unhealthy pods
- Automatically restarts failed containers

Tradeoff:
- Additional configuration and health-check overhead

## Failure Scenario

Simulated:
- Incorrect MONGO_HOST environment variable

Debugging Steps:
- kubectl get pods
- kubectl logs
- kubectl describe deployment
- Correct environment variable
- Verify application recovery
