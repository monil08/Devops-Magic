# Step 4: Setup DockerHub
**Series:** DevOps for Lazy People  

## What This Step Does

Docker Hub is like GitHub but for Docker images. It stores your containerized applications so they can be:
- Pulled and run on any machine
- Used in CI/CD pipelines
- Deployed to cloud platforms
- Shared with your team or the public

## Prerequisites

- Completed Step 3 (Dockerized Flask application)
- Docker Desktop installed and running
- GitHub account (for CI/CD integration)

## Step-by-Step Setup

### 1. Create Docker Hub Account

If you don't already have one:

1. Go to https://hub.docker.com/signup
2. Sign up with your email
3. Verify your email address
4. Login at https://hub.docker.com/

### 2. Create a Public Repository

This is where your Docker images will live.

1. Login to Docker Hub: https://hub.docker.com/
2. Click **"Repositories"** in the top menu
3. Click **"Create Repository"** button
4. Fill in the details:
   - **Repository Name**: `netflix-ka-bhai` (lowercase, no spaces)
   - **Description**: "Flask app for DevOps CI/CD demo"
   - **Visibility**: **Public** (free, no charges)
5. Click **"Create"**

Your repository URL will be: `yourusername/netflix-ka-bhai`

### 3. Generate Access Token

**Why do this?** GitHub Actions needs permission to push images to your Docker Hub. Access tokens are more secure than using your password directly.

1. Login to Docker Hub: https://hub.docker.com/
2. Click your **username** (top-right corner)
3. Click **"Account Settings"**
4. Click **"Security"** in the left sidebar
5. Click **"New Access Token"** button
6. Configure the token:
   - **Description**: `GitHub Actions CI/CD`
   - **Access permissions**: Read, Write, Delete (or just Read & Write)
7. Click **"Generate"**
8. **CRITICAL**: Copy the token NOW - you won't see it again!
`

### 4. Store Credentials in GitHub

Your CI/CD pipeline needs these credentials to push images automatically.

1. Go to your GitHub repository
2. Click the **"Settings"** tab
3. Navigate to **"Secrets and variables"** → **"Actions"** (left sidebar)
4. Click **"New repository secret"**

**Add Secret #1:**
- **Name**: `DOCKERHUB_USERNAME`
- **Value**: Your Docker Hub username
- Click **"Add secret"**

**Add Secret #2:**
- **Name**: `DOCKERHUB_TOKEN`
- **Value**: Paste the access token you copied
- Click **"Add secret"**


```powershell
# Login to Docker Hub
docker login -u yourusername
# Enter your password or access token when prompted

# Tag your image (if needed)
docker tag yourusername/flask-devops-demo:latest yourusername/flask-devops-demo:latest

# Push to Docker Hub
docker push yourusername/flask-devops-demo:latest
```

## Pull Command
```bash
docker pull yourusername/flask-devops-demo:latest
```
