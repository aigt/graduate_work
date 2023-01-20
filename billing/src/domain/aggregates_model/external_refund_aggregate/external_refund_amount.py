from decimal import Decimal

from domain.seed_work.descriptors import ValidatebleDescriptor


class ExternalRefundAmount(ValidatebleDescriptor):
    """Сумма возврата."""

    min_amount = 1

    def validate(self, value_to_validate: Decimal) -> None:
        """Валидировать значение Id.

        Args:
            value_to_validate (Decimal): Значение для валидации.

        Raises:
            ValueError: Если возврат меньше минимальной суммы.
        """
        if value_to_validate < self.minsize:
            raise ValueError(f"Expected {value_to_validate!r} to be no smaller than {self.min_amount!r}")
