from __future__ import annotations

from dataclasses import dataclass

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor, V


class ExternalPaymentIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора платежа."""

    def validate(self, value_to_validate: V) -> None:
        """Метод валидации.

        Args:
            value_to_validate (V): Значение.

        Raises:
            TypeError
        """
        if not isinstance(value_to_validate, ExternalPaymentId):
            raise TypeError()


@dataclass(frozen=True, slots=True)
class ExternalPaymentId:
    """Идентификатор платежа."""

    id: str
