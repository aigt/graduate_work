from abc import ABC, abstractmethod

from domain.aggregates_model.user_aggregate.user_id import UserId

from grpc.aio import insecure_channel

from infrastructure.auth_proto.auth_pb2 import ChangeRoleRequest, ResponseStatuses
from infrastructure.auth_proto.auth_pb2_grpc import AuthNotifyStub


class AuthService(ABC):
    """Сервис авторизации."""

    @abstractmethod
    async def add_subscriber_status(self, user_id: UserId) -> bool:

        """Добавить статус подписчика пользователю.

        Args:
            user_id (UserId): Id пользователя.
        """


class Auth(AuthService):
    """Интерфейс взаимодействия с сервисом авторизации."""

    subscriber = "subscriber"
    unsubscribe = "unsubscribe"

    def __init__(self, host: str):
        self.host = host

    async def add_subscriber_status(self, user_id: UserId) -> bool:
        """Добавить статус подписчика пользователю.

        Args:
            user_id (UUID): Id пользователя.

        Returns:
            request result(bool): Успешность запроса.
        """
        async with insecure_channel(self.host) as channel:
            stub = AuthNotifyStub(channel)
            response = stub.SetUserRole(ChangeRoleRequest(user_id=str(user_id), role=self.subscriber))
            if response == ResponseStatuses.Value("OK"):
                return True
            return False

    async def del_subscriber_status(self, user_id: UserId) -> bool:
        """Удалить статус подписчика пользователю.

        Args:
            user_id (UUID): Id пользователя.

        Returns:
            request result(bool): Успешность запроса.
        """
        async with insecure_channel(self.host) as channel:
            stub = AuthNotifyStub(channel)
            response = stub.SetUserRole(ChangeRoleRequest(user_id=str(user_id), role=self.unsubscribe))
            if response == ResponseStatuses.Value("OK"):
                return True
            return False
