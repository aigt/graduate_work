from abc import ABC, abstractmethod

from domain.aggregates_model.external_payment_aggregate.external_payment import (
    ExternalPayment,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_status import (
    ExternalPaymentStatusStripe,
)
from domain.aggregates_model.payment_aggregate.payment import Payment
from domain.aggregates_model.payment_aggregate.payment_external_id import (
    PaymentExternalId,
)
from domain.aggregates_model.payment_aggregate.payment_id import PaymentId
from domain.aggregates_model.payment_aggregate.payment_system_id import PaymentSystemId
from domain.aggregates_model.payment_aggregate.payment_user_id import PaymentUserId
from domain.aggregates_model.payment_aggregate.session_id import SessionId
from domain.aggregates_model.user_aggregate.user_id import UserId


class PaymentRepository(ABC):
    """Интерфейс репозиториев платежей."""

    @abstractmethod
    async def create_payment(
        self,
        user_id: PaymentUserId,
        external_payment: ExternalPayment,
        system_id: PaymentSystemId,
    ) -> Payment:
        """Создать платёж.

        Args:
            user_id (PaymentUserId): Идентификатор пользователя совершившего платёж.
            external_payment (ExternalPayment): Данные платежа из внешней платёжной системы.
            system_id (PaymentSystemId): Идентификатор платёжной системы, в которой выполнен платёж.

        Returns:
            Payment: Платёж.
        """

    @abstractmethod
    async def get_by_external_id(self, external_id: PaymentExternalId) -> Payment:
        """Найти платёж по идентификатору внешнего сервиса.

        Args:
            external_id (PaymentExternalId): Идентификатор платежа в платёжной системе.

        Returns:
            Payment: Платёж.
        """

    @abstractmethod
    async def get_last_by_user_id(self, user_id: UserId) -> Payment:
        """Найти последний платёж по идентификатору пользователя.

        Args:
            user_id (UserId): Идентификатор пользователя.

        Returns:
            Payment: Платёж.
        """

    @abstractmethod
    async def refund_payment(
        self,
        payment_id: PaymentId,
    ) -> None:
        """Пометить платёж как возвращённый.

        Args:
            payment_id (PaymentId): Идентификатор пользователя совершившего платёж.
        """

    @abstractmethod
    async def set_payment_id_by_payment_system(
        self,
        session_id: SessionId,
        payment_id: PaymentId,
        payment_status: ExternalPaymentStatusStripe,
    ) -> None:
        """Добавить id платежа, статус при получении вебхука stripe.

        Args:
            session_id (SessionId): Идентификатор сессии
            payment_id (PaymentId): Идентификатор сессии stripe.
            payment_status (ExternalPaymentStatusStripe): Статус платежа stripe
        """
