from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    """Простой ответ с ошибкой."""

    message: str = Field(description="Сообщение с описанием ошибки.")
