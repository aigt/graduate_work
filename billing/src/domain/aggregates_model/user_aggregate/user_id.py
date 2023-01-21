from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from domain.seed_work.descriptors import ReadOnlyValidatebleDescriptor


class UserIdField(ReadOnlyValidatebleDescriptor):
    """Дескриптор идентификатора пользователя."""

    def validate(self, value_to_validate: UserId) -> None:
        """Валидировать значение Id.

        Args:
            value_to_validate (UserId): Значение для валидации.
        """


@dataclass(frozen=True, slots=True)
class UserId:
    """Идентификатор пользователя."""

    id: UUID
