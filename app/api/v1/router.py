from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.home import router as home_router
from app.api.v1.user import router as user_router

router = APIRouter()

router.include_router(home_router)
router.include_router(user_router)
router.include_router(auth_router)
