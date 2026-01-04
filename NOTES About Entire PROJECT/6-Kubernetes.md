# Step 6: Create Kubernetes Manifests
**Series:** DevOps for Lazy People  

Complete Kubernetes deployment manifests for your Flask application. Deploy your containerized app to Kubernetes with proper configuration, scaling, and health checks.

## 📋 What This Step Does

This creates the Kubernetes manifests that define how your application runs in a cluster:
- **Deployment**: Manages your app pods, replicas, and container specs
- **Service**: Exposes your app and handles traffic routing
- **ConfigMap**: Stores configuration data separately from your code

Together, these manifests tell Kubernetes exactly how to run, scale, and expose your Flask application.

## 📁 Project Structure

```
your-project/
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── app.py
├── Dockerfile
└── (other files)
```

## 📝 Create Kubernetes Manifests

### A. Create k8s Directory

In your project folder, create the `k8s/` directory:

```
your-project/
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── app.py
├── Dockerfile
└── (other files)
```

### B. Create Deployment Manifest

Create `k8s/deployment.yaml`:

**View the complete deployment manifest here:**  
👉 [deployment.yaml](https://github.com/codewithmonil/Devops-Magic/blob/main/k8s/deployment.yaml)

**Important**: Replace `yourusername` with your actual Docker Hub username!

**What this does:**
- Creates 2 replicas (pods) of your Flask app
- Uses your Docker Hub image
- Always pulls latest image
- Exposes port 5000
- Loads config from ConfigMap
- Sets resource limits
- Health checks (liveness & readiness probes)

### C. Create Service Manifest

Create `k8s/service.yaml`:

**View the complete service manifest here:**  
👉 [service.yaml](https://github.com/codewithmonil/Devops-Magic/blob/main/k8s/service.yaml)

**What this does:**
- Exposes Flask app outside the cluster
- Type: NodePort (perfect for kind)
- Maps port 80 (service) → 5000 (container)
- NodePort: 30000 (accessible at localhost:30000)
- Routes traffic to pods labeled `app: flask-app`

### D. Create ConfigMap Manifest

Create `k8s/configmap.yaml`:

**View the complete configmap manifest here:**  
👉 [configmap.yaml](https://github.com/codewithmonil/Devops-Magic/blob/main/k8s/configmap.yaml)

**What this does:**
- Stores configuration data
- Can be updated without rebuilding images
- Used by deployment (APP_NAME, ENVIRONMENT variables)

## 🚀 Test Manifests Locally

### Apply Manifests to Your Local kind Cluster

```powershell
# Create kind cluster
kind create cluster

# Make sure your kind cluster is running
kind get clusters

# Apply all manifests
kubectl apply -f k8s/
```

**If error occurs:**
```powershell
# Check pod events
kubectl describe pod <pod-name>
# or
kubectl describe pod -l app=flask-app

# Check logs
kubectl logs <pod-name>

# Force restart deployment
kubectl rollout restart deployment/flask-app
```

### Cleanup
```bash
# Delete all resources
kubectl delete -f k8s/

# Delete cluster
kind delete cluster --name devops-demo
```

## 🔗 Manifest Files

Access all Kubernetes manifests here:
- **[deployment.yaml](https://github.com/codewithmonil/Devops-Magic/blob/main/k8s/deployment.yaml)** - Application deployment configuration
- **[service.yaml](https://github.com/codewithmonil/Devops-Magic/blob/main/k8s/service.yaml)** - Service and networking configuration
- **[configmap.yaml](https://github.com/codewithmonil/Devops-Magic/blob/main/k8s/configmap.yaml)** - Configuration data


**Made with ❤️ for lazy people who want Kubernetes without the complexity**
