from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class ExternalRefundPaymentIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора платежа для возврата."""

    def validate(self, value_to_validate: ExternalRefundPaymentId) -> None:
        """Валидировать значение Id.

        Args:
            value_to_validate (ExternalRefundPaymentId): Значение для валидации.
        """


@dataclass(frozen=True, slots=True)
class ExternalRefundPaymentId:
    """Идентификатор платежа для возврата."""

    id: UUID
