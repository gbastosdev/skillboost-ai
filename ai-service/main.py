from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from controllers import *

app = FastAPI(title="Skillboost-AI")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/call_ai")
async def post_challenge()-> JSONResponse:   
    try:
        print(123)
    except Exception as e:
        return JSONResponse(content=f"Error: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.get("/get_challenges")
async def get_challenges() -> JSONResponse:   
    try:
        print(123)
        return JSONResponse(content=f'Challenges:{11}', status_code=status.HTTP_302_FOUND)
    except Exception as e:
        return JSONResponse(content=f"Error: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    