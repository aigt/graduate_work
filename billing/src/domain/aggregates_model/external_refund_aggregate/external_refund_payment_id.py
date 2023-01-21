from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class ExternalRefundPaymentIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора платежа для возврата."""


@dataclass(frozen=True, slots=True)
class ExternalRefundPaymentId:
    """Идентификатор платежа для возврата."""

    id: UUID
