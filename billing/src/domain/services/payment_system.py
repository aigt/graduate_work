# https://yookassa.ru/developers/payment-acceptance/integration-scenarios/smart-payment
from abc import ABC, abstractmethod
from typing import NewType

from domain.aggregates_model.external_payment_aggregate.external_payment import (
    ExternalPayment,
)
from domain.aggregates_model.external_refund_aggregate.external_refund import (
    ExternalRefund,
)

PaymentId = NewType("PaymentId", str)
RefundId = NewType("RefundId", str)


class PaymentSystem(ABC):
    """Платёжная система."""

    @abstractmethod
    def create_payment(self) -> ExternalPayment:
        """Создать платёж.

        Returns:
            ExternalPayment: Созданный платёж.
        """

    @abstractmethod
    def payments(self) -> list[ExternalPayment]:
        """Получить список платежей зарегестрированных в платёжной системе.

        Returns:
            list[ExternalPayment]: Список платежей.
        """

    @abstractmethod
    def payment_by_id(self, payment_id: PaymentId) -> ExternalPayment:
        """Получить информацию о платеже в платёжной системе.

        Args:
            payment_id (PaymentId): Идентификатор платежа.

        Returns:
            PaymentInSystem: Платёж в системе.
        """

    @abstractmethod
    def capture_payment(self, payment_id: PaymentId) -> list[ExternalPayment]:
        """Подтвердить платёж в платёжной системе.

        Args:
            payment_id (PaymentId): Идентификатор платежа.

        Returns:
            PaymentInSystem: Платёж в системе.
        """

    @abstractmethod
    def cancel_payment(self, payment_id: PaymentId) -> list[ExternalPayment]:
        """Отменить платёж в платёжной системе.

        Args:
            payment_id (PaymentId): Идентификатор платежа.

        Returns:
            PaymentInSystem: Платёж в системе.
        """

    @abstractmethod
    def refunds(self) -> list[ExternalRefund]:
        """Получить список возвратов зарегестрированных в платёжной системе.

        Returns:
            list[ExternalRefund]: Список возвратов.
        """

    @abstractmethod
    def create_refund(self) -> ExternalRefund:
        """Создать возврат.

        Returns:
            ExternalRefund: Созданный возврат.
        """

    @abstractmethod
    def refund_by_id(self, refund_id: RefundId) -> ExternalRefund:
        """Получить информацию о возврате в платёжной системе.

        Args:
            refund_id (RefundId): Идентификатор возврате.

        Returns:
            ExternalRefund: Возврат в системе.
        """
