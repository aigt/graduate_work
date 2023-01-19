from uuid import UUID

from domain.seed_work.descriptor import ValidatebleDescriptor


class UserId(ValidatebleDescriptor):
    """Идентификатор пользователя."""

    def validate(self, value_to_validate: UUID) -> None:
        """Валидировать значение Id.

        Args:
            value_to_validate (UUID): Значение для валидации.
        """
