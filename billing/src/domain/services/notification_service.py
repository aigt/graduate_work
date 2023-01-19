from abc import ABC, abstractmethod
from decimal import Decimal
from uuid import UUID


class NotificationService(ABC):
    """Сервис оповещений."""

    @abstractmethod
    def notify_user_about_payment(self, user_id: UUID) -> None:
        """Оповестить пользователя о платеже.

        Args:
            user_id (UUID): Id пользователя.
        """

    @abstractmethod
    def notify_user_about_refund(self, user_id: UUID, amount: Decimal) -> None:
        """Оповестить пользователя о возврате.

        Args:
            user_id (UUID): Id пользователя.
            amount (Decimal): Сумма возврата.
        """
