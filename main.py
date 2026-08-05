from fastapi import FastAPI
import uvicorn

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI E-Commerce API!"}

if __name__ == "__main__":

    uvicorn.run("main:app", host=settings.host, port=settings.port ,reload=True)