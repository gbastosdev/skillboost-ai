from fastapi import Depends, FastAPI, status
from requests import session
from controllers.db_controller import get_db
from fastapi.responses import JSONResponse

app = FastAPI(title="Skillboost-AI")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/post_challenge")
async def post_challenge(db: session = Depends(get_db))-> JSONResponse:   
    try:
        collection = db['challenges']['challenge']
        result = collection.insert_one({ "testing" : 123 })
        return result.acknowledged
    except Exception as e:
        return JSONResponse(content=f"Error: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.get("/get_challenges")
async def get_challenges(db: session = Depends(get_db)) -> JSONResponse:   
    try:
        collection = db['challenges']['challenge']
        docs_dict = {}
        for docs in collection.find({}):
            docs_dict.update(docs)
        return JSONResponse(content=f'Challenges:{docs_dict}', status_code=status.HTTP_302_FOUND)
    except Exception as e:
        return JSONResponse(content=f"Error: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    