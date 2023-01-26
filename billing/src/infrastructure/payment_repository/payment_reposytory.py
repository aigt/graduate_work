from domain.aggregates_model.external_payment_aggregate.external_payment import (
    ExternalPayment,
)
from domain.aggregates_model.payment_aggregate.payment import Payment
from domain.aggregates_model.payment_aggregate.payment_external_id import (
    PaymentExternalId,
)
from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.aggregates_model.payment_aggregate.payment_system_id import PaymentSystemId
from domain.aggregates_model.payment_aggregate.payment_user_id import PaymentUserId


class PostgresPaymentRepository(PaymentRepository):
    """Интерфейс репозиториев платежей."""

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
        return NotImplemented

    async def get_by_external_id(self, external_id: PaymentExternalId) -> Payment:
        """Найти платёж по идентификатору внешнего сервиса.

        Args:
            external_id (PaymentExternalId): Идентификатор платежа в платёжной системе.

        Returns:
            Payment: Платёж.
        """
        return NotImplemented
