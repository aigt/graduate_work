from abc import ABC, abstractmethod
from uuid import UUID


class NotificationService(ABC):
    """Сервис оповещений."""

    @abstractmethod
    def notify_user_about_payment(self, user_id: UUID) -> None:
        """Оповестить пользователя о платеже.

        Args:
            user_id (UUID): Id пользователя.
        """
