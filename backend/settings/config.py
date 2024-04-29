import secrets
from typing import List, Optional, Any, Union
from pydantic import AnyHttpUrl, EmailStr, HttpUrl, PostgresDsn, validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []
    SECRET_KEY: str

    SQLALCHEMY_DATABASE_URI_POSTGRES: Optional[str]

    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int]

    class Config:
        env_file = ".env"


settings = Settings()