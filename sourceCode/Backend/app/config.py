import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ENCRYPTION_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    API_V1_PREFIX: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), ".env")
    )

settings = Settings()
