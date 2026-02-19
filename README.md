# 🚀 Cloud-Native FastAPI Deployment with Full CI/CD on AWS EC2

A production-style backend project demonstrating modern DevOps practices
including Docker containerization, branch-based CI/CD pipelines,
automated deployment, and environment isolation on AWS EC2.

This project simulates an enterprise-grade backend delivery workflow
using GitHub Actions and Docker Hub for continuous deployment.

------------------------------------------------------------------------

## 🏗 Architecture Overview

Local Development\
→ Git (dev / prod branches)\
→ GitHub Actions (CI/CD)\
→ Docker Hub (Image Registry)\
→ AWS EC2 (t3.micro)\
→ Docker Runtime (Environment-based containers)

------------------------------------------------------------------------

## 🧰 Technology Stack

-   **Backend Framework**: FastAPI (Python 3.10)
-   **Containerization**: Docker
-   **CI/CD**: GitHub Actions
-   **Container Registry**: Docker Hub
-   **Cloud Infrastructure**: AWS EC2 (Ubuntu 22.04, t3.micro)
-   **Deployment Method**: SSH-based automated container rollout

------------------------------------------------------------------------

## 🌐 Environment Strategy

Branch-based deployment strategy:

  Branch   Docker Tag   EC2 Port   Environment
  -------- ------------ ---------- -------------
  dev      :dev         88         Development
  prod     :prod        80         Production

This ensures environment isolation within a single EC2 instance while
maintaining deployment clarity and rollback capability.

------------------------------------------------------------------------

## 🔌 API Endpoints

### GET `/hello`

Returns:

``` json
{
  "message": "Hello World from EC2"
}
```

### POST `/hello`

Request:

``` json
{
  "name": "Your Name"
}
```

Response:

``` json
{
  "message": "Hello Your Name"
}
```

------------------------------------------------------------------------

## 🐳 Local Development

Build Docker image:

    docker build -t hello-api .

Run locally:

    docker run -d -p 8000:80 hello-api

Access:

    http://localhost:8000/hello

Swagger UI:

    http://localhost:8000/docs

------------------------------------------------------------------------

## 🔄 CI/CD Workflow

On every push to `dev` or `prod`:

1.  GitHub Actions builds Docker image
2.  Image tagged based on branch name
3.  Image pushed to Docker Hub
4.  GitHub Action connects to EC2 via SSH
5.  Latest image pulled
6.  Existing container stopped and replaced
7.  New container started with environment-specific port mapping

Fully automated deployment with no manual server interaction required.

------------------------------------------------------------------------

## 🔐 Security & Secrets Management

Sensitive credentials stored securely via GitHub Secrets:

-   DOCKERHUB_USERNAME
-   DOCKERHUB_TOKEN
-   EC2_HOST
-   EC2_USER
-   EC2_SSH_KEY

SSH-based deployment uses encrypted private key stored as a repository
secret.

------------------------------------------------------------------------

## 📈 Production Readiness Considerations

This project demonstrates:

-   Branch-based deployment model
-   Immutable Docker image strategy
-   Remote automated deployment
-   Environment separation
-   Infrastructure cost optimization (t3.micro)
-   Container lifecycle management
-   CI/CD pipeline integration

------------------------------------------------------------------------

## 🚀 Future Enhancements

-   Reverse proxy with Nginx
-   HTTPS via Let's Encrypt
-   Blue/Green deployment
-   Health checks & container restart policies
-   Migration to AWS SSM for SSH-less deployments
-   Multi-instance load balancing
-   Observability (Prometheus + Grafana)

------------------------------------------------------------------------

## 🎯 Portfolio Value

This project demonstrates hands-on experience with:

-   Cloud infrastructure provisioning
-   Container orchestration fundamentals
-   CI/CD pipeline engineering
-   DevOps automation
-   Deployment architecture design
-   Environment management strategy

Suitable for Backend Engineer, DevOps Engineer, or Cloud Engineer
portfolios.

------------------------------------------------------------------------

## 📜 License

MIT
