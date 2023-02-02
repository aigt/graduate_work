from concurrent import futures
from enum import Enum

import grpc
from auth_pb2 import ChangeRoleResponse, ResponseStatuses
from auth_pb2_grpc import AuthNotifyServicer, add_AuthNotifyServicer_to_server


class Roles(Enum):
    """Роли пользователя."""

    subscriber = "subscriber"
    unsubscribe = "unsubscribe"
    subscriber_uuid = "27fa3ba4-9778-4323-87e1-7731dfb8fd81"


class Auth(AuthNotifyServicer):
    """Сервис интерфейса gRPC."""

    def SetUserRole(self, request, context):
        """Метод для изменения роли пользователя."""
        try:
            if request.role == Roles.subscriber.value:
                return ChangeRoleResponse(status=ResponseStatuses.Value("OK"))
            elif request.role == Roles.unsubscribe.value:
                return ChangeRoleResponse(status=ResponseStatuses.Value("OK"))
        except:
            return ChangeRoleResponse(status=ResponseStatuses.Value("BAD"))
        return ChangeRoleResponse(status=ResponseStatuses.Value("BAD"))


def serve():
    """gRPC сервер."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_AuthNotifyServicer_to_server(Auth(), server)
    server.add_insecure_port("[::]:5001")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
