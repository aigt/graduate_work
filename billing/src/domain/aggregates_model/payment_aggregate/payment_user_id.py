from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class PaymentUserIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора пользователя."""


@dataclass(frozen=True, slots=True)
class PaymentUserId:
    """Идентификатор пользователя."""

    id: UUID
