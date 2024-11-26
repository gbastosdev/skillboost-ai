import os
from fastapi import FastAPI
import motor.motor_asyncio

app = FastAPI(title="Skillboost-AI")
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
