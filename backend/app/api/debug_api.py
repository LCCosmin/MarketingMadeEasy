from fastapi import APIRouter

from typing import Dict

router = APIRouter(prefix="/debug_api")


# Simple to test APIs from frontend. Will get moved to tests later
@router.post("/", response_model=Dict[str, str])
def debug_api(request: Dict[str, str] ) -> Dict[str, str]:
    print(request)
    return request
