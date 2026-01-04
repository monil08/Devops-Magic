# Step 5: Build GitHub Actions Workflow
**Series:** DevOps for Lazy People  

A complete CI/CD pipeline using GitHub Actions that automatically builds Docker images and push to dockerhub—no manual work required.

## 📋 What This Step Does

This sets up GitHub Actions to automate your entire deployment pipeline. Every time you push code to the main branch:
- GitHub Actions automatically builds a new Docker image
- Pushes it to Docker Hub with proper tags

All of this happens automatically. Push code, grab coffee, come back to a deployed app.

## 📁 Project Structure

```
your-project/
├── .github/
│   └── workflows/
│       └── ci-cd.yml      # GitHub Actions workflow file
├── k8s/                   # Kubernetes manifests (Step 7)
│   ├── deployment.yaml
│   └── service.yaml
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── kind-config.yaml
└── README.md
```

## 🔍 Understanding the Workflow

### What is GitHub Actions?
GitHub Actions is your personal DevOps robot that lives in your repository. It watches for events (like pushes) and executes automated tasks. Think of it as a 24/7 assistant that builds and deploys your code without you lifting a finger.

### The Pipeline Flow
```
Push to main → Build Docker image → Push to Docker Hub
```

### Job Structure

**Job 1: Build and Push**
- Checks out your code
- Sets up Docker Buildx (modern Docker builder)
- Logs into Docker Hub using secrets
- Builds your Docker image
- Pushes it to Docker Hub with custom tags
- Confirms success with a friendly message


### Workflow Triggers
The workflow runs automatically when:
- You push code to the `main` branch
- Someone opens a pull request to `main`
- You manually trigger it from the Actions tab (`workflow_dispatch`)

## 📝 The Complete Workflow

Access the full workflow YAML here:  
**(https://github.com/codewithmonil/Devops-Magic/blob/main/.github/workflows/ci-cd.yaml)**


