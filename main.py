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
    return {"message": f"{os.getenv('MESSAGE')}"}
