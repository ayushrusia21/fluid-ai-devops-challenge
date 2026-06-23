# Fluid AI DevOps Challenge

## Overview

This project demonstrates a production-style application deployment using Kubernetes, CI/CD, GitOps principles, and operational debugging practices.

The stack consists of:

- Flask Backend Application
- MongoDB Database
- Docker Containerization
- Kubernetes (Kind Cluster)
- GitHub Actions CI Pipeline
- ArgoCD Continuous Deployment
- Kubernetes Secret Management
- Health Checks and Resource Controls

---

# Architecture

```text
GitHub Repository
        │
        ▼
GitHub Actions (CI)
        │
        ├── Build Docker Image
        └── Push Image to Docker Hub
                    │
                    ▼
              Docker Hub
                    │
                    ▼
               ArgoCD (CD)
                    │
                    ▼
         Kind Kubernetes Cluster
                    │
      ┌─────────────┴─────────────┐
      │                           │
      ▼                           ▼
 Flask Application          MongoDB Database
 Deployment + Service      Deployment + Service
```

---

## Components

### Application

- Flask-based backend service
- Health endpoint for Kubernetes probes
- MongoDB connectivity validation

### Database

- MongoDB running as a Kubernetes Deployment
- Exposed internally using a ClusterIP Service

### Kubernetes Resources

- Namespace
- Deployments
- Services
- Secret
- Readiness Probe
- Liveness Probe
- Resource Requests and Limits

---

# CI/CD Pipeline

## Continuous Integration (GitHub Actions)

Pipeline performs:

1. Source code checkout
2. Docker image build
3. Docker Hub authentication
4. Docker image push

Trigger:

```text
Push to main branch
```

## Continuous Deployment (ArgoCD)

ArgoCD continuously monitors the Git repository and automatically synchronizes Kubernetes manifests with the cluster.

Deployment Flow:

```text
Git Commit
    ↓
GitHub Repository
    ↓
ArgoCD Detects Change
    ↓
Automatic Synchronization
    ↓
Kubernetes Cluster Updated
```

---

# Reliability Improvement

## Selected Improvement: Secret Management

Database configuration is managed through Kubernetes Secrets instead of hardcoded application configuration.

Environment variable:

```text
MONGO_HOST
```

is injected into the application using:

```text
secretKeyRef
```

### Benefits

- Separation of configuration from code
- Improved security
- Easier environment management
- Reduced risk of exposing sensitive configuration

### Tradeoffs

- Additional operational complexity
- Secret lifecycle management required
- More Kubernetes resources to maintain

---

# Additional Reliability Controls

### Readiness Probe

Ensures traffic is only routed to healthy application instances.

### Liveness Probe

Automatically restarts unhealthy containers.

### Resource Requests and Limits

Prevents uncontrolled CPU and memory consumption.

---

# Failure Simulation and Debugging

## Failure Scenario

Application deployment entered:

```text
ImagePullBackOff
```

## Symptoms

```bash
kubectl get pods -n fluid-ai
```

Application pod remained unavailable.

## Investigation

```bash
kubectl describe pod <pod-name> -n fluid-ai
```

Events revealed image pull failures.

## Root Cause

The container image was not available inside the Kind cluster.

## Resolution

```bash
kind load docker-image fluid-ai-app:latest --name fluid-ai

kubectl rollout restart deployment/fluid-ai-app -n fluid-ai
```

## Result

Application deployment recovered successfully and all pods became healthy.

---

# Verification Commands

View application resources:

```bash
kubectl get all -n fluid-ai
```

View secrets:

```bash
kubectl get secrets -n fluid-ai
```

View deployment details:

```bash
kubectl describe deployment fluid-ai-app -n fluid-ai
```

View logs:

```bash
kubectl logs deployment/fluid-ai-app -n fluid-ai
```

Port-forward application:

```bash
kubectl port-forward -n fluid-ai svc/fluid-ai-app 5000:5000
```

Test application:

```bash
curl localhost:5000

curl localhost:5000/health
```

---

# Future Improvements

For a production environment, the following enhancements would be considered:

- Managed Kubernetes (EKS / AKS / GKE)
- Prometheus and Grafana Monitoring
- Persistent Storage for MongoDB
- Helm Charts
- Image Versioning Strategy
- Multi-Environment Deployment Promotion
- Canary Deployments
- Blue-Green Deployments
- Centralized Logging
