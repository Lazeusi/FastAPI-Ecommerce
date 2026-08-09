from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
) -> UserResponse:
    service = UserService(db)

    return await service.create_user(user_data)
