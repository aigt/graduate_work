from datetime import timedelta
from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Переменные окружения."""

    postgres_host: str = Field("localhost")
    postgres_port: int = Field(5432)
    postgres_db: str = Field("payment_history")
    postgres_user: str = Field("app")
    postgres_password: str = Field("postgres")
    interval: timedelta = Field("PT10M")

    notification_url: str = Field("http://localhost:8000/api/v1/add_notification/")

    authorization_grpc_address: str = Field("[::]:443")


@lru_cache()
def get_settings() -> Settings:
    """Фабрика настроек.

    Returns:
        Settings: Класс с настройками приложения.
    """
    return Settings()
