from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from infrastructure.db.postgres import PostgresDB
from web_api.configs import logger
from web_api.configs.openapi import OpenAPISettings
from web_api.dependencies import db
from web_api.dependencies.common import get_settings
from web_api.errors.handlers import install_exception_handlers
from web_api.routers import health
from web_api.routers.v1.endpoints import payments, stripe


async def startup_event() -> None:
    """Функция выполняемая перед запуском приложения."""
    settings = get_settings()
    db.postgres = PostgresDB(postgres_dsn=settings.payments_postgres_dsn)
    await db.postgres.init_connection()


async def shutdown_event() -> None:
    """Функция выполняемая перед завершением приложения."""
    db.postgres.close_connection()


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
        docs_url=openapi_settings.api_docs_url,
        contact=openapi_settings.contact,
        openapi_url=openapi_settings.openapi_url,
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
    app.include_router(
        stripe.router,
        prefix=settings.api_v1_str + settings.api_stripe,
        tags=[openapi_settings.api_stripe_tag],
    )
    app.include_router(
        payments.router,
        prefix=settings.api_v1_str + settings.api_payments,
        tags=[openapi_settings.api_payments_tag],
    )

    return app
