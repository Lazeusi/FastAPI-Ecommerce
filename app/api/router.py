from fastapi import APIRouter

from app.core.logger import logger
from app.api.routes.home import router as home_router


api_router = APIRouter()

def create_api_router() -> APIRouter:

    api_router.include_router(home_router)
    
    return api_router