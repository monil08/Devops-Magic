# Step 1: Setup for the Project

**Series:** DevOps for Lazy People 

## What This Covers

Setting up a complete local Kubernetes development environment on Windows 11. 
You'll install Docker Desktop, kubectl (Kubernetes command-line tool), and kind (Kubernetes in Docker) to run a local cluster.

<p align="center">
  <img src="https://github.com/codewithmonil/Devops-Magic/blob/main/Project-Architecture.jpg?raw=true" alt="Project Architecture">
</p>

## The Stack

**Docker Desktop** - Runs containers on Windows, includes WSL 2 for Linux compatibility  
**kubectl** - Your command-line interface to Kubernetes clusters  
**kind** - Creates lightweight Kubernetes clusters using Docker containers, perfect for local development

## Installation Steps

### Docker Desktop

Download from docker.com/products/docker-desktop, run the installer, enable WSL 2 during setup, restart your machine. Launch Docker Desktop and verify it's working.

### kubectl

Download the binary, create a dedicated directory at C:\kubectl, move the executable there, add that directory to your system PATH so Windows can find it from anywhere. Close and reopen PowerShell to pick up the PATH change.

### kind

Similar process - download the Windows binary, create C:\kind directory, move the executable there and rename it to kind.exe, add to PATH, restart PowerShell.

### Create Your Cluster

Use kind to spin up a Kubernetes cluster named "devops-demo". This creates a single-node cluster running inside Docker, perfect for learning and testing.

## Commands

**Install Docker Desktop:**
```powershell
# After downloading DockerDesktop.exe, run it
# Enable WSL 2 when prompted, restart computer
docker --version
docker run hello-world
```

**Install kubectl:**
```powershell
# Run PowerShell as Administrator
curl.exe -LO "https://dl.k8s.io/release/v1.28.0/bin/windows/amd64/kubectl.exe"
mkdir C:\kubectl
move kubectl.exe C:\kubectl\
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\kubectl", "Machine")

# Close and reopen PowerShell
kubectl version --client
```

**Install kind:**
```powershell
# Run PowerShell as Administrator
curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.20.0/kind-windows-amd64
mkdir C:\kind
move kind-windows-amd64.exe C:\kind\kind.exe
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\kind", "Machine")

# Close and reopen PowerShell
kind version
```

**Final verification: IMPORTANT TO CHECK**
```powershell
docker ps
kubectl get nodes
kind get clusters
```

## Success Indicators

Docker ps shows running containers (might be empty initially). Kubectl get nodes displays one node called "devops-demo-control-plane" with Ready status. Kind get clusters lists "devops-demo".

## Key Takeaways

You now have a complete local Kubernetes environment without needing cloud access or multiple machines. The kind cluster runs entirely in Docker, making it easy to create, destroy, and recreate for testing. Always restart PowerShell after PATH changes for them to take effect.

---

**Note:** For macOS or Linux, refer to the necessary documentation and you're all set.
