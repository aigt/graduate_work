from functools import lru_cache

from pydantic.env_settings import BaseSettings
from pydantic.fields import Field


class Settings(BaseSettings):
    """Переменные окружения."""

    url: str = Field("http://localhost:8000/api/v1")

    postgres_user: str = Field("app")
    postgres_password: str = Field("postgres")
    postgres_users_host: str = Field("localhost")
    postgres_port: int = Field(5432)

    payments_db: str = Field("payments")


@lru_cache()
def get_settings() -> Settings:
    """Фабрика настроек.

    Returns:
        Settings: Класс с настройками приложения.
    """
    return Settings()
