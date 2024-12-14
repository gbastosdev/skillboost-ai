from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from controllers import ai_controller

ai_session = ai_controller()

app = FastAPI(title="Skillboost-AI")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/call_ai")
async def post_challenge()-> JSONResponse:   
    try:
        message = ai_session.ai_response()
        return JSONResponse(content=message)
    except Exception as e:
        return JSONResponse(content=f"Error: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
