from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class ExternalRefundIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора возврата."""

    def validate(self, value_to_validate: ExternalRefundId) -> None:
        """Валидировать значение Id.

        Args:
            value_to_validate (ExternalRefundId): Значение для валидации.
        """


@dataclass(frozen=True, slots=True)
class ExternalRefundId:
    """Идентификатор возврата."""

    id: UUID
