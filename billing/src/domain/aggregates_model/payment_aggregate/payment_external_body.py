from __future__ import annotations

from dataclasses import dataclass

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class PaymentExternalBodyField(ReadOnlyValidatebleDescriptor):
    """Дескриптор содержания платежа во внешней системе."""


@dataclass(frozen=True, slots=True)
class PaymentExternalBody:
    """Содержание платежа во внешней системе."""

    body: str
