from http import HTTPStatus

from starlette.exceptions import HTTPException as StarletteHTTPException


class HTTPException(StarletteHTTPException):
    """Базовое HTTP исключение для приложения."""

    def __init__(self, status_code: int, detail: str | None = None) -> None:
        """__init__.

        Args:
            status_code (int): Код HTTP статуса для ответа.
            detail (str): Сообщение с подробностями об ошибке. По умолчанию None.
        """
        super().__init__(status_code=status_code, detail=detail)


class BadRequestError(HTTPException):
    """Базовое Bad Request HTTP исключение для приложения."""

    def __init__(self, detail: str):
        """__init__.

        Args:
            detail (str): Сообщение с подробностями об ошибке.
        """
        super().__init__(
            status_code=HTTPStatus.BAD_REQUEST.value,
            detail=detail,
        )


class UnauthorizedError(HTTPException):
    """Базовое 401 Unauthorized HTTP исключение для приложения."""

    def __init__(self, detail: str = "Unauthorized."):
        """__init__.

        Args:
            detail (str): Сообщение с подробностями об ошибке. По умолчанию "Unauthorized.".
        """
        super().__init__(
            status_code=HTTPStatus.UNAUTHORIZED.value,
            detail=detail,
        )


class ForbiddenError(HTTPException):
    """Базовое 403 Forbidden HTTP исключение для приложения."""

    def __init__(self, detail: str = "Forbidden."):
        """__init__.

        Args:
            detail (str): Сообщение с подробностями об ошибке. По умолчанию "Forbidden.".
        """
        super().__init__(
            status_code=HTTPStatus.FORBIDDEN.value,
            detail=detail,
        )


class NotFoundError(HTTPException):
    """Базовое 404 Not Found HTTP исключение для приложения."""

    def __init__(self, detail: str = "Not found."):
        """__init__.

        Args:
            detail (str): Сообщение с подробностями об ошибке. По умолчанию "Not found.".
        """
        super().__init__(
            status_code=HTTPStatus.NOT_FOUND.value,
            detail=detail,
        )


class InternalServerError(HTTPException):
    """Базовое 500 Internal Server Error HTTP исключение для приложения."""

    def __init__(self, detail: str = "Internal Server Error."):
        """__init__.

        Args:
            detail (str): Сообщение с подробностями об ошибке. По умолчанию "Internal Server Error.".
        """
        super().__init__(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            detail=detail,
        )
