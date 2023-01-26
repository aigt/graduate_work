from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from web_api.errors.exceptions import HTTPException


async def app_http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """Хэндлер для HTTP исключений приложения.

    Args:
        request (Request): Запрос.
        exc (HTTPException): Исключение возникшее в ходе обработки запроса.

    Returns:
        JSONResponse: Детальный ответ.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


def install_exception_handlers(app: FastAPI) -> None:
    """Установить хэндлеры исключений в FastAPI приложение.

    Args:
        app (FastAPI): Приложение.
    """
    app.exception_handler(HTTPException)(app_http_exception_handler)
