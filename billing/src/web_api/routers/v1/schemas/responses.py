from pydantic import BaseModel, Field


class EmptyResponse(BaseModel):
    """Пустой ответ."""


class SimpleResponse(BaseModel):
    """Простой ответ."""

    message: str = Field(description="Сообщение о результате выполнения запроса.")


class StripeCallbackResponse(BaseModel):
    """Ответ трайпа в колюэк ответ."""

    success: str = Field(description="Подтверждение об обработке вызова (True).")
