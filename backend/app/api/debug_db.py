from typing import Dict

from fastapi import APIRouter, Depends

from sqlalchemy import select
from sqlalchemy.orm import Session

from core.database import generate_db
from models.users_data import users_data

router = APIRouter(prefix="/debug_db")


# Simple to test APIs from frontend. Will get moved to tests later
@router.get("/", response_model=Dict[str, str])
def debug_db(db: Session = Depends(generate_db)) -> Dict[str, str]:
    try:
        query = select(users_data).limit(1)
        db.execute(query).fetchall()
    except:
        return{"DEBUG_DB": "DOES NOT WORK!"}
    return {"DEBUG_DB": "WORKS!"}
