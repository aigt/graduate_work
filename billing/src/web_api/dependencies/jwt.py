from typing import Union

import fastapi
from fastapi import Security
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer

from web_api.errors.exceptions import ForbiddenError


class JWT:
    """JWT токен."""

    bearer = HTTPBearer(auto_error=False)

    async def __call__(
        self,
        auth_credentials: HTTPAuthorizationCredentials = Security(bearer),
    ) -> Union[str, fastapi.HTTPException]:
        """Получить токен из запроса.

        Args:
            auth_credentials (HTTPAuthorizationCredentials): Авторизационные реквизиты. Defaults to Security(bearer).

        Raises:
            ForbiddenError: Авторизационных реквизитов не получено.
            ForbiddenError: Авторизационные реквизиты не корректны.

        Returns:
            str: Токен.
        """
        if auth_credentials is None:
            raise ForbiddenError(detail="Not authenticated")
        if auth_credentials.credentials is None:
            raise ForbiddenError(detail="Invalid authentication credentials")
        return auth_credentials.credentials
