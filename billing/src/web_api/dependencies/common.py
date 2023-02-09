import logging
import os

from cachetools import cached  # type: ignore
from fastapi import Depends

from web_api.configs.settings import Settings
from web_api.dependencies.jwt import JWT
from web_api.services.jwt import JWTService


@cached(cache={})
def get_settings() -> Settings:
    """Фабрика настроек.

    Returns:
        Settings: Класс с настройками приложения.
    """
    logging.info("Creating and caching Settings, pid: {pid}".format(pid=os.getpid()))
    return Settings()


def get_jwt_service(
    jwt: JWT = Depends(JWT),
    settings: Settings = Depends(get_settings),
) -> JWTService:
    """Фабрика для jwt сервиса.

    Args:
        jwt (JWT): Depends(JWT).
        settings (Settings): Depends(get_settings).

    Returns:
        JWTService: Сервис по работе с JWT.
    """
    return JWTService(token=jwt.token(), auth_rsa_public_key=settings.auth_rsa_public_key)
