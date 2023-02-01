from pydantic import BaseSettings


class OpenAPISettings(BaseSettings):
    """Настройки OpenAPI документации."""

    api_docs_url: str = "/api/openapi"
    openapi_url: str = "/api/openapi.json"

    api_description = "Асинхронный API для сервиса биллинга."

    api_healthcheck_tag = "api_healthcheck"
    api_stripe_tag = "api_stripe"

    tags_metadata = [
        {
            "name": api_healthcheck_tag,
            "description": "Эндпоинт для проверки состояния api-сервиса с помощью healthcheck'ов.",
        },
        {
            "name": api_stripe_tag,
            "description": "Эндпоинт для работы со stripe сервисом.",
        },
    ]

    contact = {
        "name": "Ссылка на репозиторий GitHub",
        "url": "https://github.com/aigt/graduate_work",
    }

    class Config:
        env_prefix = "OPENAPI_"
        env_nested_delimiter = "_"
