from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Настройки приложения."""

    # Название проекта. Используется в Swagger-документации
    project_name: str = Field(default="billing")
    api_version: str = "1.0.0"

    host = "localhost"

    auth_rsa_public_key = ""

    # Роуты
    api_v1_str: str = "/api/v1"
    api_health: str = "/api/health"

    api_stripe: str = "/paysystems/stripe"
    api_payments: str = "/payments"
    api_refunds: str = "/refunds"

    # Stripe
    endpoint_secret: str = ""

    # Auth service
    auth_service_host = "localhost"
