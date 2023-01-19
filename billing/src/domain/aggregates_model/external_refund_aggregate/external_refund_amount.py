from uuid import UUID

from domain.seed_work.descriptor import ValidatebleDescriptor


class ExternalRefundAmount(ValidatebleDescriptor):
    """Сумма возврата."""

    minsize = 1

    def validate(self, value_to_validate: UUID):
        """Валидировать значение Id.

        Args:
            value_to_validate (UUID): Значение для валидации.

        Raises:
            ValueError: Если возврат меньше минимальной суммы.
        """
        if value_to_validate < self.minsize:
            raise ValueError(f"Expected {value_to_validate!r} to be no smaller than {self.minsize!r}")
