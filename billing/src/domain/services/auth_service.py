from abc import ABC, abstractmethod

from domain.aggregates_model.user_aggregate.user_id import UserId


class AuthService(ABC):
    """Сервис авторизации."""

    @abstractmethod
    async def add_subscriber_status(self, user_id: UserId) -> None:
        """Добавить статус подписчика пользователю.

        Args:
            user_id (UserId): Id пользователя.
        """

    @abstractmethod
    async def del_subscriber_status(self, user_id: UserId) -> None:
        """Удалить статус подписчика пользователю.

        Args:
            user_id (UserId): Id пользователя.

        """
