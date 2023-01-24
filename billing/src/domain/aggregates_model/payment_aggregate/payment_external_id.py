from __future__ import annotations

from dataclasses import dataclass

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class PaymentExternalIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора платежа во внешней системе."""


@dataclass(frozen=True, slots=True)
class PaymentExternalId:
    """Идентификатор платежа во внешней системе."""

    id: str
