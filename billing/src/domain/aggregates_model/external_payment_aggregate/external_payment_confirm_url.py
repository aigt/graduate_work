from __future__ import annotations

from dataclasses import dataclass

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class ExternalPaymentConfirmUrlField(ReadOnlyValidatebleDescriptor):
    """Дескриптор ссылки перенаправления пользователя на созданный платёж."""


@dataclass(frozen=True, slots=True)
class ExternalPaymentConfirmUrl:
    """Ссылка перенаправления пользователя на созданный платёж."""

    id: str
