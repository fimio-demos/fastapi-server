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
async def env_message():
    logging.info("env_var_message endpoint was called")
    return {"message": f"{os.getenv('MESSAGE', 'No message found')}"}

@app.get("/env_var_number")
async def env_number():
    logging.info("env_var_number endpoint was called")
    return {"number": f"{os.getenv('NUMBER', 'No number found')}"}
