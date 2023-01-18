# https://yookassa.ru/developers/payment-acceptance/integration-scenarios/smart-payment
from abc import ABC, abstractmethod
from typing import NewType

from domain.aggregates_model.external_payment_aggregate.external_payment import (
    ExternalPayment,
)

PaymentId = NewType("PaymentId", str)


class PaymentSystem(ABC):
    """Платёжная система."""

    @abstractmethod
    def create_payment(self) -> ExternalPayment:
        """Создать платёж."""

    @abstractmethod
    def payments(self) -> list[ExternalPayment]:
        """Получить список платежей зарегестрированных в платёжной системе."""

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
