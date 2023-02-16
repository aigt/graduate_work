from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from domain.seed_work.descriptors import V, ValidatebleDescriptor


class ExternalPaymentStatusEnum(Enum):
    """Перечисление статусов платежей."""

    PENDING = "pending"
    WAITING_FOR_CAPTURE = "waiting_for_capture"
    SUCCEDED = "succeeded"
    CANCELED = "canceled"


class ExternalPaymentStatusField(ValidatebleDescriptor):
    """Дескриптор поля статуса платежа."""

    def validate(self, value_to_validate: V) -> None:
        """Метод валидации.

        Args:
            value_to_validate (V): Значение.
        """
        if not isinstance(value_to_validate, ExternalPaymentStatus):
            raise TypeError()


@dataclass(frozen=True, slots=True)
class ExternalPaymentStatus:
    """Статус платежа."""

    status: ExternalPaymentStatusEnum
