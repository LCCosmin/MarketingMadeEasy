from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from datetime import timedelta

from app.core.database import generate_db
from app.core.settings import settings
from app.helpers.user_helpers import authenticate_user
from app.helpers.token_helpers import create_access_token
from app.models.token import Token

router = APIRouter(prefix="/login")


@router.post("/", response_model=Token)
async def login_for_access_token(
    request: OAuth2PasswordRequestForm = Depends(),
) -> Token:
    user = authenticate_user(request.username, request.password)
    if not user: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=settings.TOKEN_EXPIRATION_TIME_MINUTES)
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

