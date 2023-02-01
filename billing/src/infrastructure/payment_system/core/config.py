from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Конфиг для работы с платежными системами."""

    # Stripe config
    STRIPE_PUBLIC_KEY: str = Field(
        'pk_test_51MRWwzAQCuru3FKxT20ovetIQMdy2eLmHwzC45oewEnPambhkKSlcTPww1Jd4URywxCoxAQgIkwqprJ3UB2h8fY600MqsJtdNO',
        env='STRIPE_PUBLIC_KEY',
    )
    STRIPE_SECRET_KEY: str = Field(
        'sk_test_51MRWwzAQCuru3FKxIj5HMsfCDNzbFOInOXMIDyVXozq5Jnb0ZeESzsK4pX9aD9MK1FWUZ7uU9g1X7cp3czB9Qk3s006fYmPxbN',
        env='STRIPE_SECRET_KEY',
    )
    endpoint_secret = Field(
        'whsec_ziOrz7Z6KkFSSUjpmUh5uEoNakzIexRG',
        env='ENDPOINT_SECRET',
    )
    success_page_url = 'http://127.0.0.1:8000/api/v1/success'
    cancel_page_url = 'http://127.0.0.1:8000/api/v1/cancel'


def get_settings() -> Settings:
    """Фабрика настроек.
    Returns:
        Settings: Класс с настройками приложения.
    """
    return Settings()
