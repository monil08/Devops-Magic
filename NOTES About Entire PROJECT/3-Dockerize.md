# Step 3: Dockerized the Flask App
**Series:** DevOps for Lazy People  

A simple Flask application containerized with Docker to demonstrate the basics of application containerization and DevOps practices.

## What This Project Does

This is a basic Flask web application packaged in a Docker container. It demonstrates how to:
- Structure a Python web project for containerization
- Create a Docker image from your application
- Run your app in an isolated, reproducible environment

## Project Structure

```
your-project/
├── app.py              # Your Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker build instructions
├── .dockerignore      # Files to exclude from Docker image
└── README.md          # This file
```

## File Breakdown

### `app.py`
Your Flask application code. Contains routes and application logic.

### `requirements.txt`
Lists all Python packages your app depends on:

### `Dockerfile`
Instructions for building your Docker image:
```dockerfile
FROM python:3.11-slim       # Base image
WORKDIR /app                # Set working directory
COPY requirements.txt .     # Copy dependencies list
RUN pip install --no-cache-dir -r requirements.txt  # Install dependencies
COPY . .                    # Copy application code
EXPOSE 5000                 # Document the port
CMD ["python","app.py"]     # Command to run the app
```

### `.dockerignore`
Tells Docker which files to skip when building (cache files, git history, etc.)

## Common Commands

### Building
```powershell
# Build with a tag
docker build -t yourusername/netflix-ka-bhai:latest .
```

### Running
```powershell
# Run detached (background)
docker run -d -p 5000:5000 yourusername/netflix-ka-bhai:latest

# Run with a custom name
docker run -d -p 5000:5000 --name flask-test yourusername/netflix-ka-bhai:latest
```

### Managing Containers
```powershell
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop flask-test

# Remove a container
docker rm flask-test

# Stop and remove in one command
docker rm -f flask-test
```

### Managing Images
```powershell
# List all images
docker images

# Remove an image
docker rmi yourusername/netflix-ka-bhai:latest

# Remove all unused images
docker image prune
```

## Understanding the Pieces

### Docker Image vs Container
- **Image**: The packaged template (like a class in programming)
- **Container**: A running instance of that image (like an object)

You build images once, then create as many running containers from them as you need.

### Port Mapping
The `-p 5000:5000` flag maps:
- **Host port 5000** (your computer) → **Container port 5000** (inside Docker)

This makes the app accessible at `localhost:5000` on your machine.

### Detached Mode
The `-d` flag runs containers in the background, freeing up your terminal.

## Why Docker?

Docker solves the classic "works on my machine" problem by packaging your entire application environment. Once dockerized:
- Your app runs identically on any machine
- No dependency conflicts
- Easy to share and deploy
- Consistent development, testing, and production environments

## Next Steps

This is **Step 3** in the DevOps for Lazy People series. After mastering local Docker:
- **Step 4**: Push your image to Docker Hub
- **Step 5**: Set up CI/CD pipelines
- **Step 6**: Deploy to Kubernetes

---

**Made with ❤️ for lazy people who want to learn DevOps without the headaches**