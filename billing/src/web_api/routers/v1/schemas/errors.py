from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Простой ответ с ошибкой."""

    message: str
