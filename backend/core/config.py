from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator
import os

class Settings(BaseSettings):
    DATABASE_URL:str
    API_PREFIX:str = "/api"
    DEBUG:bool = False
    ALLOWED_ORIGINS: List[str] = []
    GROQ_API_KEY:str
    HOST_EMAIL:str
    HOST_PASSWORD:str

    # def __init__(self, **values):
    #     super().__init__(**values)
    #     if not self.DEBUG:
    #         db_user = os.getenv("DB_USER")
    #         db_password = os.getenv("DB_PASSWORD")
    #         db_host = os.getenv("DB_HOST")
    #         db_port = os.getenv("DB_PORT")
    #         db_name = os.getenv("DB_NAME")
    #         self.DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def parse_allowed_origin(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
