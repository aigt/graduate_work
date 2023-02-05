import logging
from typing import Any, Dict, Union
from uuid import UUID

import fastapi
import jose.jwt  # noqa: WPS301

from web_api.errors.exceptions import ForbiddenError


class JWTService:
    """JWT сервис."""

    def __init__(self, token: str, auth_rsa_public_key: str) -> None:
        logging.info(token)
        self._token = token
        self._auth_rsa_public_key = auth_rsa_public_key

    def token_payload(self) -> Union[Dict[str, Any], fastapi.HTTPException]:
        """Декодирование токена.

        Raises:
            ForbiddenError: Токен не удалось декодировать.

        Returns:
            Dict[str, Any]: Пэйлод токена.
        """
        try:
            return jose.jwt.decode(self._token, self._auth_rsa_public_key, "RS256")
        except jose.exceptions.JWTError as ex:
            logging.exception(ex)
            raise ForbiddenError(detail="Invalid token")

    def get_user_id(self) -> Union[UUID, fastapi.HTTPException]:
        """Получить id пользователя из пэйлода токена.

        Raises:
            ForbiddenError: Не удалось извлечь id

        Returns:
            str: id
        """
        token_payload = self.token_payload()
        if token_payload is None:
            raise ForbiddenError(detail="Empty token")
        return UUID(token_payload.get("sub", "").split()[0])
