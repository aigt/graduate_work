from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from domain.seed_work.descriptors import ValidatebleDescriptor


class PaymentAmountField(ValidatebleDescriptor):
    """Сумма платежа."""

    min_amount: Decimal = Decimal(1)

    def validate(self, value_to_validate: PaymentAmount) -> None:
        """Валидировать сумму платежа.

        Args:
            value_to_validate (PaymentAmount): Значение для валидации.

        Raises:
            ValueError: Если платёж меньше минимальной суммы.
        """
        if value_to_validate.amount < self.min_amount:
            raise ValueError(f"Expected {value_to_validate!r} to be no smaller than {self.min_amount!r}")


@dataclass(frozen=True, slots=True)
class PaymentAmount:
    """Сумма платежа."""

    amount: Decimal
