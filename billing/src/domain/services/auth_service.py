from abc import ABC, abstractmethod
from uuid import UUID


class AuthService(ABC):
    """Сервис авторизации."""

    @abstractmethod
    async def add_subscriber_status(self, user_id: UUID) -> None:
        """Добавить статус подписчика пользователю.

        Args:
            user_id (UUID): Id пользователя.
        """
