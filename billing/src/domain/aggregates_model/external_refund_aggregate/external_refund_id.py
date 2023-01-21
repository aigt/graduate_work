from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class ExternalRefundIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора возврата."""


@dataclass(frozen=True, slots=True)
class ExternalRefundId:
    """Идентификатор возврата."""

    id: UUID
