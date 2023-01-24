from __future__ import annotations

from dataclasses import dataclass

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class ExternalPaymentIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора платежа."""


@dataclass(frozen=True, slots=True)
class ExternalPaymentId:
    """Идентификатор платежа."""

    id: str
