from typing import Generator

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.settings import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocomit=False, autoflush=False, bind=engine)

base = declarative_base()

meta = MetaData()

def generate_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
