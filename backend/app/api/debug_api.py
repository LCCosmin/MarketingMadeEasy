from fastapi import APIRouter

from typing import Dict

router = APIRouter(prefix="/debug_api")


# Simple to test APIs from frontend. Will get moved to tests later
@router.get("/", response_model=Dict[str, str])
def debug_api() -> Dict[str, str]:
    return {"DEBUG_API": "WORKS!"}
