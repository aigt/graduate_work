from grpc.aio import insecure_channel

from domain.aggregates_model.user_aggregate.user_id import UserId
from domain.services.auth_service import AuthService
from infrastructure.auth_service.auth_pb2 import ChangeRoleRequest, ResponseStatuses
from infrastructure.auth_service.auth_pb2_grpc import AuthNotifyStub


class MovieAuthService(AuthService):
    """Сервис авторизации кинотеатра."""

    subscriber = "subscriber"
    unsubscribe = "unsubscribe"

    def __init__(self, host: str):
        self.host = host

    async def add_subscriber_status(self, user_id: UserId) -> bool:
        """Добавить статус подписчика пользователю.

        Args:
            user_id (UserId): Id пользователя.

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
            user_id (UserId): Id пользователя.

        Returns:
            request result(bool): Успешность запроса.
        """
        async with insecure_channel(self.host) as channel:
            stub = AuthNotifyStub(channel)
            response = stub.SetUserRole(ChangeRoleRequest(user_id=str(user_id), role=self.unsubscribe))
            if response == ResponseStatuses.Value("OK"):
                return True
            return False
