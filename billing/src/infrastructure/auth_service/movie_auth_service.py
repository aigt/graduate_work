from enum import Enum

from grpc.aio import insecure_channel

from domain.aggregates_model.user_aggregate.user_id import UserId
from domain.services.auth_service import AuthService
from infrastructure.auth_service.auth_exceptions import RoleChangeError
from infrastructure.auth_service.auth_pb2 import ChangeRoleRequest, ResponseStatuses
from infrastructure.auth_service.auth_pb2_grpc import AuthNotifyStub


class Role(Enum):
    """Роли пользователей."""

    subscriber = "subscriber"
    unsubscribe = "unsubscribe"


class MovieAuthService(AuthService):
    """Сервис авторизации кинотеатра."""

    def __init__(self, host: str):
        self.host = host

    async def add_subscriber_status(self, user_id: UserId) -> None:
        """Добавить статус подписчика пользователю.

        Args:
            user_id (UserId): Id пользователя.
        """
        await self._request_for_change_role(user_id, Role.subscriber)

    async def del_subscriber_status(self, user_id: UserId) -> None:
        """Удалить статус подписчика пользователю.

        Args:
            user_id (UserId): Id пользователя.
        """
        await self._request_for_change_role(user_id, Role.unsubscribe)

    async def _request_for_change_role(self, user_id: UserId, role: Role) -> None:
        """Запрос в сервис авторизации.

        Args:
            user_id (UserId): Id пользователя.
            role(Role): Роль задаваемая пользователю.

        Raises:
            RoleChangeError: Ошибка при запросе на изменение роли.
        """
        async with insecure_channel(self.host) as channel:
            stub = AuthNotifyStub(channel)
            response = await stub.SetUserRole(ChangeRoleRequest(user_id=str(user_id), role=role.value))
            if response == ResponseStatuses.Value("BAD"):
                raise RoleChangeError()
