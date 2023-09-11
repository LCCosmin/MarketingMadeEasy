from typing import Generator
import logging
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.settings import settings

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

print(settings.DATABASE_URI)


engine = create_engine(settings.DATABASE_URI)
connection = engine.connect()

SessionLocal = sessionmaker(autocomit=False, autoflush=False, bind=engine)

base = declarative_base()

meta = MetaData()

def generate_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
