from datetime import timedelta, datetime

from fastapi import Depends
from jose import jwt

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import generate_db
from app.schemas.secret_token import secret_token
from app.core.settings import settings


def obtain_secret_key(db: Session = Depends(generate_db)) -> str:
    query = select(secret_token.c.secret_token).where(secret_token.c.name=="jwt_secret_token")
    result = db.execute(query).fetchone()
    
    print(result)
    return result["secret_token"]

def create_access_token(data: dict, expires_delta: timedelta or None = None) -> str:
    to_encode = data.copy()
    expires_delta = (
        expires_delta + datetime.utcnow()
        if expires_delta
        else
        datetime.utcnow() + timedelta(settings.TOKEN_EXPIRATION_TIME_MINUTES)
    )
    
    to_encode.update({"exp": expires_delta})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.TOKEN_ALGORITHM)
    return encoded_jwt
