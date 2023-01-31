from __future__ import annotations

from dataclasses import dataclass

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor, V


class ExternalRefundIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора возврата."""

    def validate(self, value_to_validate: V) -> None:
        """Метод валидации.

        Args:
            value_to_validate (V): Значение.
        """
        if not isinstance(value_to_validate, ExternalRefundId):
            raise TypeError()


@dataclass(frozen=True, slots=True)
class ExternalRefundId:
    """Идентификатор возврата."""

    id: str
