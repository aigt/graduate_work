from domain.aggregates_model.external_refund_aggregate.external_refund_amount import (
    ExternalRefundAmount,
)
from domain.aggregates_model.user_aggregate.user_id import UserId
from domain.services.notification_service import NotificationService


class MovieNotificationService(NotificationService):
    """Сервис оповещений кинотеатра."""

    async def notify_user_about_payment(self, user_id: UserId) -> None:
        """Оповестить пользователя о платеже.

        Args:
            user_id (UserId): Id пользователя.
        """

    async def notify_user_about_refund(self, user_id: UserId, amount: ExternalRefundAmount) -> None:
        """Оповестить пользователя о возврате.

        Args:
            user_id (UserId): Id пользователя.
            amount (ExternalRefundAmount): Сумма возврата.
        """
