# https://yookassa.ru/developers/payment-acceptance/integration-scenarios/smart-payment
from abc import ABC, abstractmethod
from typing import NewType

from domain.aggregates_model.external_payment_aggregate.external_payment import (
    ExternalPayment,
)
from domain.aggregates_model.external_refund_aggregate.external_refund import (
    ExternalRefund,
)
from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.services.auth_service import AuthService
from domain.services.notification_service import NotificationService

PaymentId = NewType("PaymentId", str)
RefundId = NewType("RefundId", str)


class PaymentSystem(ABC):
    """Платёжная система."""

    def __init__(
        self,
        payment_repository: PaymentRepository,
        auth_service: AuthService,
        notification_service: NotificationService,
    ):
        self._payment_repository = payment_repository
        self._auth_service = auth_service
        self._notification_service = notification_service

    async def on_payment_event(
        self,
        payment_id: str,
        event: str,
    ) -> None:
        """Колбэк для событий платежа.

        Args:
            payment_id (str): Идентификатор платежа.
            event (str): Событие платежа.
        """
        payment = await self._payment_repository.get_by_external_id(payment_id)
        await self._auth_service.add_subscriber_status(payment.user_id)
        await self._notification_service.notify_user_about_payment(payment.user_id)

    @abstractmethod
    async def create_payment(self) -> ExternalPayment:
        """Создать платёж.

        Returns:
            ExternalPayment: Созданный платёж.
        """

    @abstractmethod
    async def payments(self) -> list[ExternalPayment]:
        """Получить список платежей зарегестрированных в платёжной системе.

        Returns:
            list[ExternalPayment]: Список платежей.
        """

    @abstractmethod
    async def payment_by_id(self, payment_id: PaymentId) -> ExternalPayment:
        """Получить информацию о платеже в платёжной системе.

        Args:
            payment_id (PaymentId): Идентификатор платежа.

        Returns:
            PaymentInSystem: Платёж в системе.
        """

    @abstractmethod
    async def capture_payment(self, payment_id: PaymentId) -> list[ExternalPayment]:
        """Подтвердить платёж в платёжной системе.

        Args:
            payment_id (PaymentId): Идентификатор платежа.

        Returns:
            PaymentInSystem: Платёж в системе.
        """

    @abstractmethod
    async def cancel_payment(self, payment_id: PaymentId) -> list[ExternalPayment]:
        """Отменить платёж в платёжной системе.

        Args:
            payment_id (PaymentId): Идентификатор платежа.

        Returns:
            PaymentInSystem: Платёж в системе.
        """

    @abstractmethod
    async def refunds(self) -> list[ExternalRefund]:
        """Получить список возвратов зарегестрированных в платёжной системе.

        Returns:
            list[ExternalRefund]: Список возвратов.
        """

    @abstractmethod
    async def create_refund(self) -> ExternalRefund:
        """Создать возврат.

        Returns:
            ExternalRefund: Созданный возврат.
        """

    @abstractmethod
    async def refund_by_id(self, refund_id: RefundId) -> ExternalRefund:
        """Получить информацию о возврате в платёжной системе.

        Args:
            refund_id (RefundId): Идентификатор возврате.

        Returns:
            ExternalRefund: Возврат в системе.
        """
