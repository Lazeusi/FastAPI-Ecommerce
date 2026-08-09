from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserResponse
from app.utils.password import hash_password


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    async def create_user(self, user_data: UserCreate) -> UserResponse:
        existing_user = await self.repository.get_by_email(user_data.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email is already registered.",
            )

        hashed_password = hash_password(user_data.password)

        user = await self.repository.create(
            email=user_data.email,
            hashed_password=hashed_password,
        )

        return UserResponse.model_validate(user)
