from __future__ import annotations

from dataclasses import dataclass

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class SessionIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора сессии."""


@dataclass(frozen=True, slots=True)
class SessionId:
    """Идентификатор сессии."""

    id: str
