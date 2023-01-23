from abc import ABC, abstractmethod

from domain.aggregates_model.external_refund_aggregate.external_refund_amount import (
    ExternalRefundAmount,
)
from domain.aggregates_model.user_aggregate.user_id import UserId


class NotificationService(ABC):
    """Сервис оповещений."""

    @abstractmethod
    async def notify_user_about_payment(self, user_id: UserId) -> None:
        """Оповестить пользователя о платеже.

        Args:
            user_id (UserId): Id пользователя.
        """

    @abstractmethod
    async def notify_user_about_refund(self, user_id: UserId, amount: ExternalRefundAmount) -> None:
        """Оповестить пользователя о возврате.

        Args:
            user_id (UserId): Id пользователя.
            amount (ExternalRefundAmount): Сумма возврата.
        """
