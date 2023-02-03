from fastapi import Depends

from web_api.configs.settings import Settings
from web_api.dependencies.jwt import JWT
from web_api.services.jwt import JWTService


def get_settings() -> Settings:
    """Фабрика настроек.

    Returns:
        Settings: Класс с настройками приложения.
    """
    return Settings()


def get_jwt_service(
    jwt: str = Depends(JWT),
    settings: Settings = Depends(get_settings),
) -> JWTService:
    """Фабрика для jwt сервиса.

    Args:
        jwt (str): Depends(JWT).
        settings (Settings): Depends(get_settings).

    Returns:
        JWTService: Сервис по работе с JWT.
    """
    return JWTService(token=jwt, auth_rsa_public_key=settings.auth_rsa_public_key)
