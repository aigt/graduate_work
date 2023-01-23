from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class PaymentIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора платежа."""


@dataclass(frozen=True, slots=True)
class PaymentId:
    """Идентификатор платежа."""

    id: UUID
