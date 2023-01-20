from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.services.auth_service import AuthService
from domain.services.notification_service import NotificationService


class PaymentSystemCallback:
    """Сервис обработки событий платежей."""

    def __init__(
        self,
        payment_repository: PaymentRepository,
        auth_service: AuthService,
        notification_service: NotificationService,
    ):
        self._payment_repository = payment_repository
        self._auth_service = auth_service
        self._notification_service = notification_service

    def on_payment_event(
        self,
        payment_id: str,
        event: str,
    ) -> None:
        """Колбэк для событий платежа.

        Args:
            payment_id (str): Идентификатор платежа.
            event (str): Событие платежа.
        """
        payment = self._payment_repository.get_by_external_id(payment_id)
        self._auth_service.add_subscriber_status(payment.user_id)
        self._notification_service.notify_user_about_payment(payment.user_id)
