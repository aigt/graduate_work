from errors.handlers import install_exception_handlers
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from web_api.config import logger
from web_api.config.openapi import OpenAPISettings
from web_api.dependencies.common import get_settings
from web_api.routers import health


async def startup_event() -> None:
    """Функция выполняемая перед запуском приложения."""


async def shutdown_event() -> None:
    """Функция выполняемая перед завершением приложения."""


def build() -> FastAPI:
    """Собрать FastAPI.

    Returns:
        FastAPI: Настроенное FastAPI приложение.
    """
    logger.configure_logging()

    settings = get_settings()
    openapi_settings = OpenAPISettings()

    app = FastAPI(
        title=settings.project_name,
        description=openapi_settings.api_description,
        openapi_tags=openapi_settings.tags_metadata,
        version=settings.api_version,
        docs_url=settings.api_docs_url,
        contact=openapi_settings.contact,
        openapi_url=settings.openapi_url,
        default_response_class=ORJSONResponse,
    )

    install_exception_handlers(app)

    app.on_event("startup")(startup_event)
    app.on_event("shutdown")(shutdown_event)

    app.include_router(
        health.router,
        prefix=settings.api_health,
        tags=[openapi_settings.api_healthcheck_tag],
    )

    return app
