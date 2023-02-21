from abc import ABC, abstractmethod

from domain.aggregates_model.external_payment_aggregate.external_payment import (
    ExternalPayment,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_amount import (
    ExternalPaymentAmount,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_id import (
    ExternalPaymentId,
)
from domain.aggregates_model.external_refund_aggregate.external_refund import (
    ExternalRefund,
)
from domain.aggregates_model.external_refund_aggregate.external_refund_amount import (
    ExternalRefundAmount,
)
from domain.aggregates_model.external_refund_aggregate.external_refund_id import (
    ExternalRefundId,
)
from domain.aggregates_model.external_refund_aggregate.external_refund_payment_id import (
    ExternalRefundPaymentId,
)
from domain.aggregates_model.payment_aggregate.payment_external_id import (
    PaymentExternalId,
)
from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.aggregates_model.user_aggregate.user_id import UserId
from domain.services.auth_service import AuthService
from domain.services.notification_service import NotificationService


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
        payment = await self._payment_repository.get_by_external_id(PaymentExternalId(id=payment_id))
        await self._auth_service.add_subscriber_status(payment.user_id.id)
        await self._notification_service.notify_user_about_payment(payment.user_id.id)

    async def on_refunded_event(self, user_id: UserId) -> None:
        """Событие возврата платежа.

        Args:
            user_id (UserId): Идентификатор пользователя.
        """
        await self._auth_service.del_subscriber_status(user_id)

    @property
    @abstractmethod
    def system_id(self) -> str:
        """Идентификатор платёжной системы.

        Returns:
            str: Идентификатор.
        """

    @abstractmethod
    async def create_payment(self, amount: ExternalPaymentAmount) -> ExternalPayment:
        """Создать платёж.

        Args:
            amount (ExternalPaymentAmount): Сумма платежа.

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
    async def payment_by_id(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Получить информацию о платеже в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе.
        """

    @abstractmethod
    async def capture_payment(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Подтвердить платёж в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе.
        """

    @abstractmethod
    async def cancel_payment(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Отменить платёж в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе.
        """

    @abstractmethod
    async def refunds(self) -> list[ExternalRefund]:
        """Получить список возвратов зарегестрированных в платёжной системе.

        Returns:
            list[ExternalRefund]: Список возвратов.
        """

    @abstractmethod
    async def create_refund(self, amount: ExternalRefundAmount, payment_id: ExternalRefundPaymentId) -> ExternalRefund:
        """Создать возврат.

        Args:
            amount (ExternalRefundAmount): Сумма возврата.
            payment_id (ExternalRefundPaymentId): Идентификатор платежа, на который осуществляется возврат.

        Returns:
            ExternalRefund: Созданный возврат.
        """

    @abstractmethod
    async def refund_by_id(self, refund_id: ExternalRefundId) -> ExternalRefund:
        """Получить информацию о возврате в платёжной системе.

        Args:
            refund_id (ExternalRefundId): Идентификатор возврата.

        Returns:
            ExternalRefund: Возврат в системе в актуальном состоянии.
        """
