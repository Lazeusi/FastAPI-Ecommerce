from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.user import UserRepository
from app.schemas.auth import LoginRequest, TokenResponse
from app.utils.jwt import create_access_token
from app.utils.password import verify_password


class AuthService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    async def login(self, credentials: LoginRequest) -> TokenResponse:
        user = await self.repository.get_by_email(credentials.email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        if not verify_password(
            credentials.password,
            user.hashed_password,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User account is inactive.",
            )

        access_token = create_access_token(str(user.id))

        return TokenResponse(
            access_token=access_token,
        )
