from http import HTTPStatus
from typing import Any

from starlette.exceptions import HTTPException as StarletteHTTPException


class HTTPException(StarletteHTTPException):
    """Базовое HTTP исключение для приложения."""

    def __init__(
        self,
        status_code: int,
        error_code: int,
        detail: Any = None,
    ) -> None:
        """__init__.

        Args:
            status_code (int): Код HTTP статуса для ответа.
            error_code (int): Код ошибки, уникальный для всего приложения.
            detail (Any): Сообщение с подробностями об ошибке. По умолчанию None.
        """
        super().__init__(status_code=status_code, detail=detail)
        self.error_code = error_code


class BadRequestError(HTTPException):
    """Базовое Bad Request HTTP исключение для приложения."""

    def __init__(self, error_code: int, detail: Any):
        """__init__.

        Args:
            error_code (int): Код ошибки, уникальный для всего приложения.
            detail (Any): Сообщение с подробностями об ошибке.
        """
        super().__init__(
            error_code=error_code,
            status_code=HTTPStatus.BAD_REQUEST.value,
            detail=detail,
        )


class UnauthorizedError(HTTPException):
    """Базовое 401 Unauthorized HTTP исключение для приложения."""

    def __init__(
        self,
        error_code: int = 401,
        detail: Any = "Unauthorized.",
    ):
        """__init__.

        Args:
            error_code (int): Код ошибки, уникальный для всего приложения. По умолчанию 401.
            detail (Any): Сообщение с подробностями об ошибке. По умолчанию "Unauthorized.".
        """
        super().__init__(
            error_code=error_code,
            status_code=HTTPStatus.UNAUTHORIZED.value,
            detail=detail,
        )


class ForbiddenError(HTTPException):
    """Базовое 403 Forbidden HTTP исключение для приложения."""

    def __init__(
        self,
        error_code: int = 403,
        detail: Any = "Forbidden.",
    ):
        """__init__.

        Args:
            error_code (int): Код ошибки, уникальный для всего приложения. По умолчанию 403.
            detail (Any): Сообщение с подробностями об ошибке. По умолчанию "Forbidden.".
        """
        super().__init__(
            error_code=error_code,
            status_code=HTTPStatus.FORBIDDEN.value,
            detail=detail,
        )


class NotFoundError(HTTPException):
    """Базовое 404 Not Found HTTP исключение для приложения."""

    def __init__(
        self,
        error_code: int = 404,
        detail: Any = "Not found.",
    ):
        """__init__.

        Args:
            error_code (int): Код ошибки, уникальный для всего приложения. По умолчанию 404.
            detail (Any): Сообщение с подробностями об ошибке. По умолчанию "Not found.".
        """
        super().__init__(
            error_code=error_code,
            status_code=HTTPStatus.NOT_FOUND.value,
            detail=detail,
        )


class InternalServerError(HTTPException):
    """Базовое 500 Internal Server Error HTTP исключение для приложения."""

    def __init__(
        self,
        error_code: int = 500,
        detail: Any = "Internal Server Error.",
    ):
        """__init__.

        Args:
            error_code (int): Код ошибки, уникальный для всего приложения. По умолчанию 500.
            detail (Any): Сообщение с подробностями об ошибке. По умолчанию "Internal Server Error.".
        """
        super().__init__(
            error_code=error_code,
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            detail=detail,
        )
