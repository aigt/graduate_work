import os
from logging import config as logging_config
from core.logger import LOGGING
from functools import lru_cache
from pydantic import BaseSettings, Field

logging_config.dictConfig(LOGGING)

PROJECT_NAME = os.getenv('PROJECT_NAME', 'payment_service')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


"""Конфиг."""


class Settings(BaseSettings):
    """Настройки приложения."""
    STRIPE_PUBLIC_KEY: str = Field(
        "pk_test_51MRWwzAQCuru3FKxT20ovetIQMdy2eLmHwzC45oewEnPambhkKSlcTPww1Jd4URywxCoxAQgIkwqprJ3UB2h8fY600MqsJtdNO",
        env="STRIPE_PUBLIC_KEY",
    )
    STRIPE_SECRET_KEY: str = Field(
        "sk_test_51MRWwzAQCuru3FKxIj5HMsfCDNzbFOInOXMIDyVXozq5Jnb0ZeESzsK4pX9aD9MK1FWUZ7uU9g1X7cp3czB9Qk3s006fYmPxbN",
        env="STRIPE_SECRET_KEY",
    )
    endpoint_secret = 'whsec_ziOrz7Z6KkFSSUjpmUh5uEoNakzIexRG'


@lru_cache()
def get_settings() -> Settings:
    """Фабрика настроек.

    Returns:
        Settings: Класс с настройками приложения.
    """
    return Settings()
