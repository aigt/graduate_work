from abc import ABC, abstractmethod

from domain.aggregates_model.user_aggregate.user_id import UserId
from infrastructure.auth_service.movie_auth_service import MovieAuthService


class AuthService(ABC):
    """Сервис авторизации."""

    @abstractmethod
    async def add_subscriber_status(self, user_id: UserId) -> bool:
        """Добавить статус подписчика пользователю.

        Args:
            user_id (UserId): Id пользователя.
        """


class Auth(AuthService):
    """Сервис авторизации."""

    def __init__(self, movie_auth_service: MovieAuthService):
        self.auth_service = movie_auth_service

    async def add_subscriber_status(self, user_id: UserId) -> bool:
        """Добавить статус подписчика пользователю.

        Args:
            user_id (UserId): Id пользователя.

        Returns:
            request result(bool): Успешность запроса.
        """
        if await self.auth_service.add_subscriber_status(user_id):
            return True
        return False

    async def del_subscriber_status(self, user_id: UserId) -> bool:
        """Удалить статус подписчика пользователю.

        Args:
            user_id (UserId): Id пользователя.

        Returns:
            request result(bool): Успешность запроса.
        """
        if await self.auth_service.del_subscriber_status(user_id):
            return True
        return False
