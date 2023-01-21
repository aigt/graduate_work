from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from domain.seed_work.descriptors import ValidatebleDescriptor


class ExternalRefundStatusEnum(Enum):
    """Перечисление статусов возвратов."""

    PENDING = "pending"
    SUCCEDED = "succeeded"
    CANCELED = "canceled"


class ExternalRefundStatusField(ValidatebleDescriptor):
    """Дескриптор поля статуса возврата."""


@dataclass(frozen=True, slots=True)
class ExternalRefundStatus:
    """Статус возврата."""

    status: ExternalRefundStatusEnum
