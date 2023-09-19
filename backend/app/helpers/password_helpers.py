from app.core.settings import settings

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return settings.PWD_CONTEXT.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return settings.PWD_CONTEXT.hash(password)
