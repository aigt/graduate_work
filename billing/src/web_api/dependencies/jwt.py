from fastapi import Security
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer

from web_api.errors.exceptions import ForbiddenError


class JWT:
    """JWT токен."""

    bearer = HTTPBearer(auto_error=False)

    def __init__(
        self,
        auth_credentials: HTTPAuthorizationCredentials = Security(bearer),
    ) -> None:
        """__init__.

        Args:
            auth_credentials (HTTPAuthorizationCredentials): Авторизационные реквизиты. Defaults to Security(bearer).
        """
        self._auth_credentials = auth_credentials

    def token(self) -> str:
        """Получить токен из запроса.

        Raises:
            ForbiddenError: Авторизационных реквизитов не получено.
            ForbiddenError: Авторизационные реквизиты не корректны.

        Returns:
            str: JWT.
        """
        if self._auth_credentials is None:
            raise ForbiddenError(detail="Not authenticated")
        if self._auth_credentials.credentials is None:
            raise ForbiddenError(detail="Invalid authentication credentials")
        return self._auth_credentials.credentials  # type: ignore
