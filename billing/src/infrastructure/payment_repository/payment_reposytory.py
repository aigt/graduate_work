from psycopg import AsyncConnection
from psycopg.rows import dict_row

from domain.aggregates_model.external_payment_aggregate.external_payment import (
    ExternalPayment,
)
from domain.aggregates_model.payment_aggregate.payment import Payment
from domain.aggregates_model.payment_aggregate.payment_amount import PaymentAmount
from domain.aggregates_model.payment_aggregate.payment_external_body import (
    PaymentExternalBody,
)
from domain.aggregates_model.payment_aggregate.payment_external_id import (
    PaymentExternalId,
)
from domain.aggregates_model.payment_aggregate.payment_id import PaymentId
from domain.aggregates_model.payment_aggregate.payment_refunded import PaymentRefunded
from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.aggregates_model.payment_aggregate.payment_system_id import PaymentSystemId
from domain.aggregates_model.payment_aggregate.payment_user_id import PaymentUserId


class PostgresPaymentRepository(PaymentRepository):
    """Интерфейс репозиториев платежей."""

    def __init__(self, connect: AsyncConnection):
        self.connect = connect

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
        async with self.connect.cursor() as cur:
            await cur.execute(
                """
                INSERT INTO payments.payments(
                user_id, amount, external_id, external_payment, refunded, system_id
                )
                VALUES ('{user_id}', {amount}, '{external_id}', '{external_payment}', {refunded}, '{system_id}')
                """.format(
                    user_id=user_id.id,
                    amount=external_payment.amount.amount,
                    external_id=external_payment.id.id,
                    external_payment=external_payment.to_json(),
                    refunded=False,
                    system_id=system_id.id,
                ),
            )
            await self.connect.commit()
        return Payment(
            id=PaymentId(external_payment.id.id),
            user_id=user_id,
            amount=PaymentAmount(external_payment.amount.amount),
            external_id=PaymentExternalId(external_payment.id.id),
            external_payment=PaymentExternalBody(external_payment.to_json()),
            refunded=PaymentRefunded(False),
            system_id=system_id,
        )

    async def get_by_external_id(self, external_id: PaymentExternalId) -> Payment:
        """Найти платёж по идентификатору внешнего сервиса.

        Args:
            external_id (PaymentExternalId): Идентификатор платежа в платёжной системе.

        Returns:
            Payment: Платёж.
        """
        async with self.connect.cursor(row_factory=dict_row) as cur:
            await cur.execute(
                """
                SELECT *
                FROM payments.payments
                WHERE external_id = '{external_id}'
                """.format(
                    external_id=external_id.id,
                ),
            )
            payment: dict = await cur.fetchone()
            return Payment(
                id=PaymentId(payment.get("id")),
                user_id=PaymentUserId(payment.get("user_id")),
                amount=PaymentAmount(payment.get("amount")),
                external_id=PaymentExternalId(payment.get("external_id")),
                external_payment=PaymentExternalBody(payment.get("external_payment")),
                refunded=PaymentRefunded(payment.get("refunded")),
                system_id=PaymentSystemId(payment.get("system_id")),
            )
