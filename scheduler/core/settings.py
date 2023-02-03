from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Переменные окружения."""

    postgres: str = Field("dbname = pyment_history user=app password=postgres host=localhost port=5432")
    interval: int = Field(600)


@lru_cache()
def get_settings() -> Settings:
    """Фабрика настроек.

    Returns:
        Settings: Класс с настройками приложения.
    """
    return Settings()
