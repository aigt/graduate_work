import time
import uuid
from typing import Any

import jose.jwt as jwt
from settings import get_settings


def get_token(user_id: str) -> Any:
    """Создание токена для тестов.

    Args:
        user_id(str): идентификатор пользователя

    Returns:
        jwt(Any): токен
    """
    exp = time.time()
    payload = {
        "agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "exp": exp + 6000,
        "fresh": False,
        "iat": exp,
        "is_superuser": False,
        "jti": uuid.uuid4().hex,
        "nbf": exp - 1,
        "roles": "",
        "sub": user_id,
        "type": "access",
    }
    return jwt.encode(payload, get_settings().auth_private_key, algorithm="RS256")
