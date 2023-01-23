from __future__ import annotations

from dataclasses import dataclass

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class PaymentRefundedField(ReadOnlyValidatebleDescriptor):
    """Дескриптор поля указывающего что платёж возвращён."""


@dataclass(frozen=True, slots=True)
class PaymentRefunded:
    """Поле указывающего что платёж возвращён."""

    refunded: bool
