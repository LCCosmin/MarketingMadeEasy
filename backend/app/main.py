from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import debug_api, debug_db
from core.settings import settings

origins = [
    "http://localhost:4200",
    "http://localhost:5432",
]

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url=f"{settings.APP_PREFIX}/docs",
    openapi_url=f"{settings.APP_PREFIX}/openapi.json",
)

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["GET", "POST"], allow_headers=["*"]
)

main_router = APIRouter()

main_router.include_router(debug_api.router, tags=["debug_api"])
main_router.include_router(debug_db.router, tags=["debug_db"])

@app.on_event("startup")
def startup_func() -> None:
    print("Startup Print ?")

@main_router.get("/version_details/")
def read_version():
    return "0.0.1"

@main_router.get("/")
async def root():
    return {"message": "Hellow from main!"}

app.include_router(main_router, prefix=settings.APP_PREFIX)
