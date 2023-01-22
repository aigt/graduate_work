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
from domain.services.payment_system import PaymentSystem


class StripePaymentSystem(PaymentSystem):
    """Платёжная система Stripe.

    Документация по API внешнего сервиса доступна по ссылке:
    https://stripe.com/docs/api
    """

    async def create_payment(self, amount: ExternalPaymentAmount) -> ExternalPayment:
        """Создать платёж.

        Args:
            amount (ExternalPaymentAmount): Сумма платежа.

        Returns:
            ExternalPayment: Созданный платёж.
        """
        return NotImplemented

    async def payments(self) -> list[ExternalPayment]:
        """Получить список платежей зарегестрированных в платёжной системе.

        Returns:
            list[ExternalPayment]: Список платежей в актуальном состоянии.
        """
        return NotImplemented

    async def payment_by_id(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Получить информацию о платеже в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе в актуальном состоянии.
        """
        return NotImplemented

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
        return NotImplemented

    async def create_refund(self, amount: ExternalRefundAmount, payment_id: ExternalRefundPaymentId) -> ExternalRefund:
        """Создать возврат.

        Args:
            amount (ExternalRefundAmount): Сумма возврата.
            payment_id (ExternalRefundPaymentId): Идентификатор платежа, на который осуществляется возврат.

        Returns:
            ExternalRefund: Созданный возврат.
        """
        return NotImplemented

    async def refund_by_id(self, refund_id: ExternalRefundId) -> ExternalRefund:
        """Получить информацию о возврате в платёжной системе.

        Args:
            refund_id (ExternalRefundId): Идентификатор возврата.

        Returns:
            ExternalRefund: Возврат в системе в актуальном состоянии.
        """
        return NotImplemented
