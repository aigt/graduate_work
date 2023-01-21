# https://yookassa.ru/developers/payment-acceptance/integration-scenarios/smart-payment
from domain.aggregates_model.external_payment_aggregate.external_payment import (
    ExternalPayment,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_id import (
    ExternalPaymentId,
)
from domain.aggregates_model.external_refund_aggregate.external_refund import (
    ExternalRefund,
)
from domain.aggregates_model.external_refund_aggregate.external_refund_id import (
    ExternalRefundId,
)
from domain.services.payment_system import PaymentSystem


class YookassaPaymentSystem(PaymentSystem):
    """Платёжная система ЮKassa."""

    async def create_payment(self) -> ExternalPayment:
        """Создать платёж.

        Returns:
            ExternalPayment: Созданный платёж.
        """
        return NotImplemented

    async def payments(self) -> list[ExternalPayment]:
        """Получить список платежей зарегестрированных в платёжной системе.

        Returns:
            list[ExternalPayment]: Список платежей.
        """
        return NotImplemented

    async def payment_by_id(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Получить информацию о платеже в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе.
        """
        return NotImplemented

    async def capture_payment(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Подтвердить платёж в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе.
        """
        return NotImplemented

    async def cancel_payment(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Отменить платёж в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе.
        """
        return NotImplemented

    async def refunds(self) -> list[ExternalRefund]:
        """Получить список возвратов зарегестрированных в платёжной системе.

        Returns:
            list[ExternalRefund]: Список возвратов.
        """
        return NotImplemented

    async def create_refund(self) -> ExternalRefund:
        """Создать возврат.

        Returns:
            ExternalRefund: Созданный возврат.
        """
        return NotImplemented

    async def refund_by_id(self, refund_id: ExternalRefundId) -> ExternalRefund:
        """Получить информацию о возврате в платёжной системе.

        Args:
            refund_id (ExternalRefundId): Идентификатор возврате.

        Returns:
            ExternalRefund: Возврат в системе.
        """
        return NotImplemented
