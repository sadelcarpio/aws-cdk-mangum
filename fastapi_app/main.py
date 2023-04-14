from fastapi import FastAPI
from api.api_v1.api import router as api_router
from mangum import Mangum

app = FastAPI(
    openapi_url='/openapi.json',
    root_path='/test-fastapi'
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)
