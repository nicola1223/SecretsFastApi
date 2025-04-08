"""Main file of microservice"""
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    """API root endpoint"""
    return {'message': 'Welcome to the Wallet API!'}
