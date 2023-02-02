import uuid
from decimal import Decimal

from yookassa import Configuration, Payment, Refund

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
from domain.aggregates_model.external_refund_aggregate.external_refund_status import (
    ExternalRefundStatus,
)
from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.services.auth_service import AuthService
from domain.services.notification_service import NotificationService
from domain.services.payment_system import PaymentSystem


class YookassaPaymentSystem(PaymentSystem):
    """Платёжная система Юкасса.

    Документация по API внешнего сервиса доступна по ссылке:
    https://yookassa.ru/developers/payment-acceptance/integration-scenarios/smart-payment
    """

    def __init__(
        self,
        payment_repository: PaymentRepository,
        auth_service: AuthService,
        notification_service: NotificationService,
        redirect_url: str,
        account_id: str,
        secret_key: str,
        capture: bool = True,
        limit: int = 100,
    ):
        super().__init__(payment_repository, auth_service, notification_service)

        self.redirect_url = redirect_url
        self.limit = limit
        self.capture = capture
        Configuration.account_id = account_id
        Configuration.secret_key = secret_key

    @property
    async def system_id(self) -> str:
        """Идентификатор платёжной системы.

        Returns:
            str: Идентификатор.
        """
        return "yookassa"

    async def create_payment(self, amount: ExternalPaymentAmount) -> ExternalPayment:
        """Создать платёж.

        Args:
            amount (ExternalPaymentAmount): Сумма платежа.

        Returns:
            ExternalPayment: Созданный платёж.
        """
        payment = Payment.create(
            {
                "amount": {"value": amount, "currency": "RUB"},
                "confirmation": {"type": "redirect", "return_url": self.redirect_url},
                "description": "Subscribe",
                "capture": self.capture,
            },
            uuid.uuid4(),
        )
        return ExternalPayment(
            id=ExternalPaymentId(id=payment.id),
            amount=ExternalPaymentAmount(amount=Decimal(amount)),
            status=ExternalPaymentStatus(payment.status),
            confirm_url=ExternalPaymentConfirmUrl(payment.confirmation),
        )

    async def payments(self) -> list[ExternalPayment]:
        """Получить список платежей зарегистрированных в платёжной системе.

        Returns:
            list[ExternalPayment]: Список платежей в актуальном состоянии.
        """
        list_payments = Payment.list({"status": "succeeded", "limit": self.limit})
        return [
            ExternalPayment(
                id=ExternalPaymentId(id=payment.id),
                amount=ExternalPaymentAmount(amount=Decimal(payment.amount.value)),
                status=ExternalPaymentStatus(payment.status),
                confirm_url=ExternalPaymentConfirmUrl(payment.confirmation),
            )
            for payment in list_payments.items
        ]

    async def payment_by_id(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Получить информацию о платеже в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе в актуальном состоянии.
        """
        payment = Payment.find_one(payment_id)
        return ExternalPayment(
            id=ExternalPaymentId(id=payment.id),
            amount=ExternalPaymentAmount(amount=Decimal(payment.amount.value)),
            status=ExternalPaymentStatus(payment.status),
            confirm_url=ExternalPaymentConfirmUrl(payment.confirmation),
        )

    async def capture_payment(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Подтвердить платёж в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе в актуальном состоянии.
        """
        response = Payment.capture(payment_id, {"amount": {"value": "100.00", "currency": "RUB"}}, str(uuid.uuid4()))
        return ExternalPayment(
            id=ExternalPaymentId(id=response.id),
            amount=ExternalPaymentAmount(amount=Decimal(response.amount.value)),
            status=ExternalPaymentStatus(response.status),
            confirm_url=ExternalPaymentConfirmUrl(response.confirmation),
        )

    async def cancel_payment(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Отменить платёж в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе в актуальном состоянии.
        """
        response = Payment.cancel(payment_id, uuid.uuid4())
        return ExternalPayment(
            id=ExternalPaymentId(id=response.id),
            amount=ExternalPaymentAmount(amount=Decimal(response.amount.value)),
            status=ExternalPaymentStatus(response.status),
            confirm_url=ExternalPaymentConfirmUrl(response.confirmation),
        )

    async def refunds(self) -> list[ExternalRefund]:
        """Получить список возвратов зарегистрированных в платёжной системе.

        Returns:
            list[ExternalRefund]: Список возвратов в актуальном состоянии.
        """
        list_refunds = Refund.list({"status": "succeeded", "limit": self.limit})
        return [
            ExternalRefund(
                id=ExternalRefundId(id=payment.id),
                amount=ExternalRefundAmount(amount=Decimal(payment.amount.value)),
                status=ExternalRefundStatus(payment.status),
                payment_id=ExternalRefundPaymentId(id=payment.id),
            )
            for payment in list_refunds.items
        ]

    async def create_refund(self, amount: ExternalRefundAmount, payment_id: ExternalRefundPaymentId) -> ExternalRefund:
        """Создать возврат.

        Args:
            amount (ExternalRefundAmount): Сумма возврата.
            payment_id (ExternalRefundPaymentId): Идентификатор платежа, на который осуществляется возврат.

        Returns:
            ExternalRefund: Созданный возврат.
        """
        payment = Refund.create({"amount": {"value": amount, "currency": "RUB"}, "payment_id": payment_id})
        return ExternalRefund(
            id=ExternalRefundId(id=payment.id),
            amount=ExternalRefundAmount(amount=Decimal(payment.amount.value)),
            status=ExternalRefundStatus(payment.status),
            payment_id=ExternalRefundPaymentId(id=payment.id),
        )

    async def refund_by_id(self, refund_id: ExternalRefundId) -> ExternalRefund:
        """Получить информацию о возврате в платёжной системе.

        Args:
            refund_id (ExternalRefundId): Идентификатор возврата.

        Returns:
            ExternalRefund: Возврат в системе в актуальном состоянии.
        """
        payment = Refund.find_one(refund_id)
        return ExternalRefund(
            id=ExternalRefundId(id=payment.id),
            amount=ExternalRefundAmount(amount=Decimal(payment.amount.value)),
            status=ExternalRefundStatus(payment.status),
            payment_id=ExternalRefundPaymentId(id=payment.id),
        )
