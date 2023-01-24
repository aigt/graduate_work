from __future__ import annotations

from dataclasses import dataclass

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class PaymentSystemIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора платёжной системы, в которой выполнен платёж."""


@dataclass(frozen=True, slots=True)
class PaymentSystemId:
    """Идентификатор платёжной системы, в которой выполнен платёж."""

    id: str
