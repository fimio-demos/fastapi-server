# FastAPI Hello World Demo

A lightweight, high-performance API demonstration showcasing the power and simplicity of FastAPI.

## Features

- Interactive Swagger UI documentation
- Simple "Hello World" endpoint
- Health check endpoint
- Pydantic models for response validation

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn

## Installation

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  

# Install dependencies
pip install fastapi uvicorn
```

## Running the Application

```bash
# Run directly with Python
python main.py

# For development purposes
fastapi dev main.py

# For production deployments
fastapi run
```

## API Documentation

Once the server is running, you can access:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

- `GET /`: Returns "Hello World" message
- `GET /health`: Health check endpoint

