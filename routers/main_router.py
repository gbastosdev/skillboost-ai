from fastapi import FastAPI
from database import db_controller

app = FastAPI(title="Skillboost-AI")

db_conn = db_controller.db()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/query_db")
async def root():   
    print(123)
