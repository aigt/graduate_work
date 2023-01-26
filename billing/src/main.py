import uvicorn
from fastapi import FastAPI

from web_api import builder


def create_app() -> FastAPI:
    """Создать FastAPI приложение.

    Returns:
        FastAPI: приложение.
    """
    return builder.build()


def local_start() -> None:
    """Фунция для локального запуска приложения."""
    config = uvicorn.Config(
        "main:create_app",
        host="0.0.0.0",  # noqa: S104
        port=8000,  # noqa: WPS432
        log_level="debug",
    )
    server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    local_start()
