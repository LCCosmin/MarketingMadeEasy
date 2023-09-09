from typing import Generator

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

from app.core.settings import settings

engine = create_engine(settings.DATABASE_URI)

SessionLocal = sessionmaker(autocomit=False, autoflush=False, bind=engine)

meta = MetaData(bind=engine)

def generate_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
