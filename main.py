from fastapi import FastAPI
from routers import main_router

app = FastAPI(title="Skillboost-AI")

app.mount("/", app=main_router)
