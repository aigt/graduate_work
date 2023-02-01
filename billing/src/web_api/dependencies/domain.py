from fastapi import Depends

from domain.aggregates_model.user_aggregate.user import User
from domain.aggregates_model.user_aggregate.user_id import UserId
from web_api.dependencies.common import get_jwt_service
from web_api.services.jwt import JWTService


def get_user(jwt_service: JWTService = Depends(get_jwt_service)) -> User:
    """Фабрика пользователей.

    Args:
        jwt_service (JWTService): Depends(get_jwt_service).

    Returns:
        User: Сущность пользователя.
    """
    user_id = UserId(id=jwt_service.get_user_id())
    return User(id=user_id)
