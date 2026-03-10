# MLOps Assignment: Iris Classifier with CI/CD Pipeline

This project demonstrates a production-ready MLOps workflow for building, testing, and deploying a machine learning model using **FastAPI**, **Docker**, and **GitHub Actions**.

## Project Overview

In this assignment, we developed a complete CI/CD pipeline that automates the lifecycle of an Iris flower classifier. Every time code is pushed to the repository, the pipeline automatically trains the model, runs unit tests, builds a Docker image, and pushes it to Docker Hub.

---

## 🚀 What We Did

### 1. Model Building (`train_model.py`)
- **Dataset**: Used the classic **Iris dataset** from `sklearn`.
- **Model**: Trained a **Random Forest Classifier** to categorize flowers into three species based on 4 features (sepal length, sepal width, petal length, petal width).
- **Artifact**: Exported the trained model to `model.pkl`.

### 2. FastAPI Application (`app.py`)
- Developed a REST API using **FastAPI**.
- **Endpoint `/predict`**: Accepts a JSON payload with 4 features and returns the predicted species class (0, 1, or 2).
- **Endpoint `/`**: Simple health check to verify the API and model status.

### 3. Containerization (`Dockerfile`)
- Created a lightweight Docker image using `python:3.10-slim`.
- Configured the environment to install dependencies from `requirements.txt`.
- Exposed port `8000` and configured `uvicorn` as the web server.

### 4. CI/CD Pipeline (`.github/workflows/ci.yml`)
Implemented a robust GitHub Actions workflow that triggers on every `push` or `pull_request` to the `main` branch:
1. **Checkout**: Pulls the latest code from GitHub.
2. **Setup**: Configures Python 3.10.
3. **Install**: Installs all required libraries (`pip install -r requirements.txt`).
4. **Train**: Runs `train_model.py` to generate the latest model weights.
5. **Test**: Executes **Pytest** (`test_app.py`) to verify API logic and prediction accuracy.
6. **Login**: Authenticates with Docker Hub using secure GitHub Secrets.
7. **Build & Push**: Builds the Docker image and pushes it to `yankee2004/iris-ml-api:latest`.
8. **Verify**: Environmentally pulls the new image and runs a live prediction test to ensure the container is production-ready.

---

## 🛠️ Setup & Usage

### 1. GitHub Secrets Configuration
To enable the automated deployment, the following secrets must be added to your GitHub repository (**Settings > Secrets and variables > Actions**):
- `DOCKER_USERNAME`: `yankee2004`
- `DOCKER_PASSWORD`: Your Docker Hub Personal Access Token (PAT)

### 2. Running Locally (Docker)
You can manually pull and run the production image built by the CI/CD pipeline:
```bash
docker pull yankee2004/iris-ml-api:latest
docker run -d -p 8000:8000 --name iris-api yankee2004/iris-ml-api:latest
```

### 3. Testing the API
Once the container is running, test it with `curl`:
```bash
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```
**Expected Output:** `{"prediction": 0}`

---

## ✅ CI/CD Status
The pipeline ensures that:
- [x] Code is always testable.
- [x] Model is always fresh.
- [x] Docker image is always in sync with the latest code changes.
- [x] Deployment is fully automated.
