from fastapi import APIRouter

from app.core.logger import logger

router = APIRouter( 
    prefix="/home",
    tags=["Home"],)

@router.get("/",)
async def root():
    logger.info("Root endpoint accessed")
    return {"message": " World"}