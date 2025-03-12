import os

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: SecretStr
    SECRET_KEY: SecretStr
    ALGORITHM: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
    )


settings = Settings()


def get_db_url():
    return (
        f'postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD.get_secret_value()}@'
        f'{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'
    )


def get_auth_data():
    return {'secret_key': settings.SECRET_KEY.get_secret_value(), 'algorithm': settings.ALGORITHM}
