from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from domain.seed_work.descriptors import ValidatebleDescriptor


class ExternalPaymentStatusEnum(Enum):
    """Перечисление статусов платежей."""

    PENDING = "pending"
    WAITING_FOR_CAPTURE = "waiting_for_capture"
    SUCCEDED = "succeeded"
    CANCELED = "canceled"


class ExternalPaymentStatusField(ValidatebleDescriptor):
    """Дескриптор поля статуса платежа."""


@dataclass(frozen=True, slots=True)
class ExternalPaymentStatus:
    """Статус платежа."""

    status: ExternalPaymentStatusEnum
