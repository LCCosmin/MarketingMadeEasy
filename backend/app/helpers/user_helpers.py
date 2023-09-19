from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

from sqlalchemy import select, and_
from sqlalchemy.orm import Session
from typing import Union

from app.models.user import User
from app.core.database import generate_db
from app.core.settings import settings
from app.schemas.users_data import users_data
from app.schemas.users_credentials import users_credentials
from app.helpers.password_helpers import get_password_hash


def check_if_user_exists(username: str, db: Session = Depends(generate_db)) -> Union[str, bool]:
    query = (
        select(users_data.c.id, users_data.c.username)
        .where(
            users_data.c.username==username,
        )
    )
    
    result = db.execute(query).fetchone()
    return result["id"] if result else False

def check_password_for_user(user_id: str, password: str, db: Session = Depends(generate_db)) ->bool:
    query = (
        select(users_credentials.c.id)
        .where(
            and_(
                users_credentials.c.id==user_id,
                users_credentials.c.hashed_password==get_password_hash(password),
            )
        )
    )

    result = db.execute(query).fetchone()
    return True if result else False

def authenticate_user(
    username: str,
    password:str,
) -> Union[User, None]:
    user = User(username, password)
    user_id = check_if_user_exists(user.username)
    
    if user_id is False:
        return None
    
    user_credential_correctiness = check_password_for_user(user_id, user.password)
    
    return user if user_credential_correctiness else None

async def get_current_user(token: str = Depends(settings.OAUTH2_SCHEME)) -> bool:
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.TOKEN_ALGORITHM])
        username: str = payload.get("sub")
        
        if username is None:
            raise credential_exception
    except JWTError:
        raise credential_exception
    
    user_exists = check_if_user_exists(username)
    
    return True if user_exists else False
