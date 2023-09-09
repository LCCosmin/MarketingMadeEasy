from pathlib import Path

from pydantic import AnyUrl
from pydantic_settings import BaseSettings

project_root = Path(__file__).parent.parent.parent

class Settings(BaseSettings):
    PROJECT_NAME: str = "MarketingMadeEasy"
    APP_PREFIX: str = "/api"

    DATABASE_URI: AnyUrl

settings = Settings(_env_file=Path(project_root, ".env"), _env_file_encoding="utf-8")
