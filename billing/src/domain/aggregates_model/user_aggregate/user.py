from uuid import UUID

from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.services.payment_system import PaymentSystem


class User:
    """Пользователь кинотеатра."""

    id: UUID

    def pay_for_subscription(
        self,
        payment_system: PaymentSystem,
        payment_repository: PaymentRepository,
    ):
        """Оплатить подписку.

        Args:
            payment_system (PaymentSystem): Платёжная система.
            payment_repository (PaymentRepository): Репозторий платежей.
        """
        ext_payment = payment_system.create_payment()
        payment_repository.create_payment(ext_payment)
