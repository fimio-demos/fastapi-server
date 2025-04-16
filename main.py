import logging
from fastapi import FastAPI
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
async def root():
    logging.info("Hello World endpoint was called")
    return {"message": "Hello World"}

@app.get("/env_var_message")
async def root():
    logging.info("Custom endpoint was called")
    message = os.getenv('MESSAGE') or "Environment variable MESSAGE not set"
    return {"message": message}

@app.get("/env_var_number")
async def root():
    logging.info("Custom endpoint was called")
    return {"number": f"{os.getenv('NUMBER')}"}
