from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from typing import Dict

from app.core.database import generate_db

router = APIRouter(prefix="/debug")


@router.get("/", response_model=Dict[str, str])
def debug_api(request: Dict[str, str], db: Session = Depends(generate_db)) -> Dict[str, str]:
    ok_message_key = f"{request.keys()} + 1"
    ok_message_value = f"{request.values} + 2"

    return {ok_message_key: ok_message_value}
