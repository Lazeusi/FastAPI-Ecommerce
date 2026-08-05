from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from app.api.router import create_api_router
from app.core.logger import logger
from app.core.config import settings 


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting {settings.app_name} v{settings.app_version}")
    yield
    logger.info(f"Shutting down {settings.app_name} v{settings.app_version}")
    
    
    
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)

app.include_router(create_api_router())

    
@app.get("/")
async def root():

    logger.info("Root endpoint accessed")
    return {"message": f"{settings.app_name} is running!"}

if __name__ == "__main__":

    uvicorn.run("main:app", host=settings.host, port=settings.port ,reload=True)