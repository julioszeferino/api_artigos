from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    
    API_V1_STR: str = '/api/v1'
    BD_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/faculdades"
    DB_BASE_MODEL = declarative_base() # Base model para declarar as entidades do modelo

    JWT_SECRET: str = 'yHXKahDXmk4USjRNW6IAIz56R5pufmMYDMqiqGeMXu' # Chave secreta para gerar o token
    """
    import secrets
    tamanho_token = 32
    token: str = secrets.token_urlsafe(tamanho_token)
    """
    ALGORITHM: str = 'HS256' # sha256
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 dias

    class Config:
        case_sensitive = True # jwt_secret <> JWT_SECRET

settings = Settings()
