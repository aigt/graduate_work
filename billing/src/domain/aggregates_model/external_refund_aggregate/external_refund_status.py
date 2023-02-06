from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from domain.seed_work.descriptors import V, ValidatebleDescriptor


class ExternalRefundStatusEnum(Enum):
    """Перечисление статусов возвратов."""

    PENDING = "pending"
    SUCCEDED = "succeeded"
    CANCELED = "canceled"


class ExternalRefundStatusField(ValidatebleDescriptor):
    """Дескриптор поля статуса возврата."""

    def validate(self, value_to_validate: V) -> None:
        """Метод валидации.

        Args:
            value_to_validate (V): Значение.
        """
        if not isinstance(value_to_validate, ExternalRefundStatus):
            raise TypeError()


@dataclass(frozen=True, slots=True)
class ExternalRefundStatus:
    """Статус возврата."""

    status: ExternalRefundStatusEnum
