from decimal import Decimal

from domain.aggregates_model.external_payment_aggregate.external_payment import (
    ExternalPayment,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_amount import (
    ExternalPaymentAmount,
)
from domain.aggregates_model.external_refund_aggregate.external_refund_amount import (
    ExternalRefundAmount,
)
from domain.aggregates_model.external_refund_aggregate.external_refund_payment_id import (
    ExternalRefundPaymentId,
)
from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.aggregates_model.payment_aggregate.payment_system_id import PaymentSystemId
from domain.aggregates_model.payment_aggregate.payment_user_id import PaymentUserId
from domain.aggregates_model.user_aggregate.user_id import UserId, UserIdField
from domain.services.payment_system import PaymentSystem


class User:
    """Пользователь кинотеатра."""

    id: UserId = UserIdField()

    def __init__(self, id: UserId) -> None:  # noqa: WPS125
        self.id = id  # noqa: WPS601

    async def pay_for_subscription(
        self,
        subscription_price: Decimal,
        payment_system: PaymentSystem,
        payment_repository: PaymentRepository,
    ) -> ExternalPayment:
        """Оплатить подписку.

        Args:
            subscription_price (Decimal): Стоимость подписки.
            payment_system (PaymentSystem): Платёжная система.
            payment_repository (PaymentRepository): Репозторий платежей.

        Returns:
            ExternalPayment: Данные о созданном платеже.
        """
        amount = ExternalPaymentAmount(amount=subscription_price)
        ext_payment: ExternalPayment = await payment_system.create_payment(amount=amount)
        await payment_repository.create_payment(
            user_id=PaymentUserId(id=self.id.id),
            external_payment=ext_payment,
            system_id=PaymentSystemId(id=payment_system.system_id),
        )
        return ext_payment

    async def refund_subscription(
        self,
        payment_system: PaymentSystem,
        payment_repository: PaymentRepository,
    ) -> None:
        """Возвратить деньги за подписку.

        Args:
            payment_system (PaymentSystem): Платёжная система.
            payment_repository (PaymentRepository): Репозторий платежей.
        """
        payment = await payment_repository.get_last_by_user_id(user_id=self.id.id)

        amount = ExternalRefundAmount(payment.amount.amount)
        external_id = ExternalRefundPaymentId(id=payment.external_id)
        await payment_system.create_refund(amount=amount, payment_id=external_id)

        await payment_repository.refund_payment(payment_id=payment.id)
