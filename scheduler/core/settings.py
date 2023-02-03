from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Переменные окружения."""

    postgres_host: str = Field("localhost")
    postgres_port: int = Field(5432)
    postgres_db: str = Field("payment_history")
    postgres_user: str = Field("app")
    postgres_password: str = Field("postgres")
    interval: int = Field(600)


@lru_cache()
def get_settings() -> Settings:
    """Фабрика настроек.

    Returns:
        Settings: Класс с настройками приложения.
    """
    return Settings()
