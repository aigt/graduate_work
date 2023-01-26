from domain.aggregates_model.user_aggregate.user_id import UserId
from domain.services.auth_service import AuthService


class MovieAuthService(AuthService):
    """Сервис авторизации кинотеатра."""

    async def add_subscriber_status(self, user_id: UserId) -> None:
        """Добавить статус подписчика пользователю.

        Args:
            user_id (UserId): Id пользователя.
        """
