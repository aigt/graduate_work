from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Настройки приложения."""

    # Название проекта. Используется в Swagger-документации
    project_name: str = Field(default="billing")
    api_version: str = "1.0.0"

    api_v1_str: str = "/api/v1"
    api_health: str = "/api/health"
