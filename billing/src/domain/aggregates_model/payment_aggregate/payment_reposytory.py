from abc import ABC, abstractmethod

from domain.aggregates_model.payment_aggregate.payment import Payment


class PaymentRepository(ABC):
    """Интерфейс репозиториев платежей."""

    @abstractmethod
    async def create_payment(self) -> Payment:
        """Создать платёж.

        Returns:
            Payment: Платёж.
        """

    @abstractmethod
    async def get_by_external_id(self, external_id: str) -> Payment:
        """Найти платёж по идентификатору внешнего сервиса.

        Args:
            external_id (str): Идентификатор платежа в платёжной системе.

        Returns:
            Payment: Платёж.
        """
