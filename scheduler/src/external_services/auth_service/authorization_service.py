from enum import Enum

from grpc import insecure_channel

from src.external_services.auth_service.auth_exceptions import RoleChangeError
from src.external_services.auth_service.auth_pb2 import (
    ChangeRoleRequest,
    ResponseStatuses,
)
from src.external_services.auth_service.auth_pb2_grpc import AuthNotifyStub


class Role(Enum):
    """Роли пользователей."""

    subscriber = "subscriber"
    unsubscribe = "unsubscribe"


class AuthorizationService:
    """Сервис авторизации кинотеатра."""

    def __init__(self, host: str):
        self.host = host

    def del_subscriber_status(self, user_id: str) -> None:
        """Удалить статус подписчика пользователю.

        Args:
            user_id (str): Id пользователя.
        """
        self._request_for_change_role(user_id, Role.unsubscribe)

    def _request_for_change_role(self, user_id: str, role: Role) -> None:
        """Запрос в сервис авторизации.

        Args:
            user_id (str): Id пользователя.
            role(Role): Роль задаваемая пользователю.

        Raises:
            RoleChangeError: Ошибка при запросе на изменение роли.
        """
        with insecure_channel(self.host) as channel:
            stub = AuthNotifyStub(channel)
            response = stub.SetUserRole(ChangeRoleRequest(user_id=str(user_id), role=role.value))
            if response == ResponseStatuses.Value("BAD"):
                raise RoleChangeError()
