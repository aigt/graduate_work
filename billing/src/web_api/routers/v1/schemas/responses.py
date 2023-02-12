from pydantic import BaseModel


class EmptyResponse(BaseModel):
    """Пустой ответ."""


class SimpleResponse(BaseModel):
    """Простой ответ."""

    message: str


class StripeCallbackResponse(BaseModel):
    """Ответ трайпа в колюэк ответ."""

    message: str
