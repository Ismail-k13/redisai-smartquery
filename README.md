# RedisAI SmartQuery System

## Overview

The **RedisAI SmartQuery System** is a structured and modular Python-based project designed to integrate ONNX models with RedisAI. It allows users to validate, load, and query machine learning models using RedisAI in a containerized environment. The system is ideal for developers and data engineers looking to serve AI models efficiently with Redis as the inference backend.

> **Project Status:** This project is currently under active development. Initial components like ONNX validation, Docker-based RedisAI setup, and inference test scripts are completed. Smart querying logic, APIs, and monitoring integrations are in progress.

## Objectives

* Load and serve ONNX models using RedisAI.
* Validate model compatibility and structure before deployment.
* Automate RedisAI container deployment using Docker Compose.
* Establish a reliable pipeline for querying models using Python scripts.
* Lay a foundation for future enhancements such as REST APIs or batch inference systems.

## Key Features

* ONNX model validation prior to loading.
* RedisAI container orchestration using Docker.
* Redis client integration for loading and testing models.
* Connectivity and inference verification.
* Clean modular script structure for extensibility.

## System Architecture

The system architecture follows a straightforward and scalable flow:

1. **validate\_model.py** checks ONNX model integrity and compatibility.
2. **load\_model.py** loads the validated model into RedisAI using `AI.MODELSET`.
3. **test\_connection.py** verifies RedisAI connectivity and confirms successful model registration.

RedisAI runs as a container using the official RedisAI image. Scripts connect to it via the Redis client to perform operations.

## Technology Stack

* **Language:** Python 3.8+
* **AI Backend:** RedisAI (via Docker)
* **Model Format:** ONNX (ResNet-50)
* **Orchestration:** Docker Compose
* **Redis Client:** `redis-py`

## Project Structure

* `docker-compose.yml` – Configuration to deploy RedisAI container.
* `requirements.txt` – Python dependencies.
* `validate_model.py` – Validates the ONNX model using the `onnx` library.
* `load_model.py` – Loads the ONNX model into RedisAI via Python.
* `test_connection.py` – Confirms RedisAI model registration and server availability.
* `model/resnet50.onnx` – The ONNX model used for deployment.

## Setup Instructions

### 1. Clone the Repository

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/redisai-smartquery.git
cd redisai-smartquery
```

### 2. Launch RedisAI via Docker Compose

Start the RedisAI container:

```bash
docker-compose up -d
```

RedisAI will be available at `localhost:6379`.

### 3. Install Python Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 4. Validate the ONNX Model

Run the ONNX validation script to ensure model integrity:

```bash
python validate_model.py
```

### 5. Load the Model into RedisAI

Use the following command to load the model:

```bash
python load_model.py
```

### 6. Test the Connection and Inference Readiness

Verify the model is correctly loaded into RedisAI:

```bash
python test_connection.py
```

## Manual RedisAI Interaction (Optional)

You can also connect to the container and run RedisAI commands manually:

```bash
docker exec -it redisai_container redis-cli
```

Example Redis command:

```bash
AI.INFO resnet_model
```

## Scripts Summary

| Script               | Purpose                                                               |
| -------------------- | --------------------------------------------------------------------- |
| `validate_model.py`  | Ensures the ONNX model is structurally valid                          |
| `load_model.py`      | Loads the model into RedisAI using Python’s Redis client              |
| `test_connection.py` | Validates RedisAI server connectivity and confirms model registration |


## Planned Enhancements

* Smart query inference module
* Support for dynamic tensor input and shape transformations
* Batch inference processing
* RESTful API and web service exposure
* Logging and monitoring integration using Prometheus/Grafana
* CI/CD integration for automated model deployment

## Contribution

Contributions are welcome. Please fork the repository and open a pull request with your proposed changes. For any issues or suggestions, please open a GitHub issue.
