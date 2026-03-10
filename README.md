# CI/CD Pipeline Implementation

This folder contains the complete CI/CD setup for deploying an Iris classifier using FastAPI and Docker via GitHub Actions.

## Setup Instructions for GitHub

1. Push this repository code to `main`.
2. Navigate to your repository's **Settings > Secrets and variables > Actions**.
3. Create the following Repository secrets:
   - `DOCKER_USERNAME`: Your Docker Hub username (`yankee2004`)
   - `DOCKER_PASSWORD`: Your Personal Access Token for DockerHub

Every time code is pushed, GitHub actions will trigger to run tests via `pytest`, build the docker image automatically, push it to dockerhub, and test running the remote container.
