from decimal import Decimal

import stripe

from domain.aggregates_model.external_payment_aggregate.external_payment import (
    ExternalPayment,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_amount import (
    ExternalPaymentAmount,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_confirm_url import (
    ExternalPaymentConfirmUrl,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_id import (
    ExternalPaymentId,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_status import (
    ExternalPaymentStatus,
    ExternalPaymentStatusEnum,
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
from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.services.auth_service import AuthService
from domain.services.notification_service import NotificationService
from domain.services.payment_system import PaymentSystem


class StripePaymentSystem(PaymentSystem):
    """Платёжная система Stripe.

    Документация по API внешнего сервиса доступна по ссылке:
    https://stripe.com/docs/api
    """

    def __init__(
        self,
        payment_repository: PaymentRepository,
        auth_service: AuthService,
        notification_service: NotificationService,
        success_url: str,
        cancel_url: str,
        stripe_secret_key: str,
        limit: int = 100,
    ):
        super().__init__(payment_repository, auth_service, notification_service)

        self.success_url = success_url
        self.cancel_url = cancel_url
        self.limit = limit
        stripe.api_key = stripe_secret_key

    @property
    def system_id(self) -> str:
        """Идентификатор платёжной системы.

        Returns:
            str: Идентификатор.
        """
        return "stripe"

    async def create_payment(self, amount: ExternalPaymentAmount) -> ExternalPayment:
        """Создать платёж.

        Args:
            amount (ExternalPaymentAmount): Сумма платежа.

        Returns:
            ExternalPayment: Созданный платёж.
        """
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": amount.amount * Decimal("100"),  # Значение в центах
                        "product_data": {
                            "name": "Subscription",
                            "description": "some description",
                        },
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=self.cancel_url,
            cancel_url=self.cancel_url,
        )
        return ExternalPayment(
            id=ExternalPaymentId(id=session.id),
            amount=ExternalPaymentAmount(amount=Decimal(session.amount_total)),
            status=ExternalPaymentStatus(status=ExternalPaymentStatusEnum.PENDING),
            confirm_url=ExternalPaymentConfirmUrl(id=session.url),
        )

    async def payments(self) -> list[ExternalPayment]:
        """Получить список платежей зарегистрированных в платёжной системе.

        Returns:
            list[ExternalPayment]: Список платежей в актуальном состоянии.
        """
        list_payments = []
        payments = stripe.PaymentIntent.list(limit=self.limit)
        for payment in payments.auto_paging_iter():
            payment_obj = ExternalPayment(
                id=payment.id,
                amount=payment.amount,
                status=payment.status,
                confirm_url="",
            )
            list_payments.append(payment_obj)
        return list_payments

    async def payment_by_id(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Получить информацию о платеже в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе в актуальном состоянии.
        """
        payment = stripe.PaymentIntent.retrieve(payment_id)
        return ExternalPayment(
            id=payment.id,
            amount=payment.amount,
            status=payment.status,
            confirm_url="",
        )

    async def capture_payment(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Подтвердить платёж в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе в актуальном состоянии.
        """
        return NotImplemented

    async def cancel_payment(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Отменить платёж в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе в актуальном состоянии.
        """
        return NotImplemented

    async def refunds(self) -> list[ExternalRefund]:
        """Получить список возвратов зарегестрированных в платёжной системе.

        Returns:
            list[ExternalRefund]: Список возвратов в актуальном состоянии.
        """
        refunds_list = []
        refunds = stripe.Refund.list(limit=100)
        for refund in refunds.auto_paging_iter():
            refund_obj = ExternalRefund(
                id=refund.id,
                amount=refund.amount,
                status=refund.status,
                payment_id=refund.payment_intent,
            )
            refunds_list.append(refund_obj)
        return refunds_list

    async def create_refund(self, amount: ExternalRefundAmount, payment_id: ExternalRefundPaymentId) -> ExternalRefund:
        """Создать возврат.

        Args:
            amount (ExternalRefundAmount): Сумма возврата.
            payment_id (ExternalRefundPaymentId): Идентификатор платежа, на который осуществляется возврат.

        Returns:
            ExternalRefund: Созданный возврат.
        """
        refund = stripe.Refund.create(payment_intent=payment_id, amount=amount)
        return ExternalRefund(
            id=refund.id,
            amount=refund.amount,
            status=refund.status,
            payment_id=refund.payment_intent,
        )

    async def refund_by_id(self, refund_id: ExternalRefundId) -> ExternalRefund:
        """Получить информацию о возврате в платёжной системе.

        Args:
            refund_id (ExternalRefundId): Идентификатор возврата.

        Returns:
            ExternalRefund: Возврат в системе в актуальном состоянии.
        """
        refund_info = stripe.Refund.retrieve(refund_id)
        return ExternalRefund(
            id=refund_info.id,
            amount=refund_info.amount,
            status=refund_info.status,
            payment_id=refund_info.payment_intent,
        )
