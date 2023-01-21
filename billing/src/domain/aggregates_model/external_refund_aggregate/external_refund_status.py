from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from enum import Enum

from domain.seed_work.descriptors import ValidatebleDescriptor


class ExternalRefundStatusEnum(Enum):
    """Перечисление статусов возвратов."""

    PENDING = "pending"
    SUCCEDED = "succeeded"
    CANCELED = "canceled"


class ExternalRefundStatusField(ValidatebleDescriptor):
    """Дескриптор статуса возврата."""

    min_amount: Decimal = Decimal(1)

    def validate(self, value_to_validate: ExternalRefundStatus) -> None:
        """Валидировать значение Id.

        Args:
            value_to_validate (ExternalRefundStatus): Значение для валидации.
        """


@dataclass(frozen=True, slots=True)
class ExternalRefundStatus:
    """Статус возврата."""

    status: ExternalRefundStatusEnum
