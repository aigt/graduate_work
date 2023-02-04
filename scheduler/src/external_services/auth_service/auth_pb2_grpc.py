# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import infrastructure.auth_service.auth_pb2 as auth__pb2


class AuthNotifyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUserData = channel.unary_stream(
            "/AuthNotify/GetUserData",
            request_serializer=auth__pb2.UsersDataRequest.SerializeToString,
            response_deserializer=auth__pb2.UsersDataResponse.FromString,
        )
        self.GetUserDataFromUsersId = channel.unary_stream(
            "/AuthNotify/GetUserDataFromUsersId",
            request_serializer=auth__pb2.UsersIds.SerializeToString,
            response_deserializer=auth__pb2.UsersDataResponse.FromString,
        )
        self.SetUserRole = channel.unary_unary(
            "/AuthNotify/SetUserRole",
            request_serializer=auth__pb2.ChangeRoleRequest.SerializeToString,
            response_deserializer=auth__pb2.ChangeRoleResponse.FromString,
        )


class AuthNotifyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUserData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetUserDataFromUsersId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SetUserRole(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AuthNotifyServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetUserData": grpc.unary_stream_rpc_method_handler(
            servicer.GetUserData,
            request_deserializer=auth__pb2.UsersDataRequest.FromString,
            response_serializer=auth__pb2.UsersDataResponse.SerializeToString,
        ),
        "GetUserDataFromUsersId": grpc.unary_stream_rpc_method_handler(
            servicer.GetUserDataFromUsersId,
            request_deserializer=auth__pb2.UsersIds.FromString,
            response_serializer=auth__pb2.UsersDataResponse.SerializeToString,
        ),
        "SetUserRole": grpc.unary_unary_rpc_method_handler(
            servicer.SetUserRole,
            request_deserializer=auth__pb2.ChangeRoleRequest.FromString,
            response_serializer=auth__pb2.ChangeRoleResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("AuthNotify", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class AuthNotify(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUserData(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/AuthNotify/GetUserData",
            auth__pb2.UsersDataRequest.SerializeToString,
            auth__pb2.UsersDataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetUserDataFromUsersId(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/AuthNotify/GetUserDataFromUsersId",
            auth__pb2.UsersIds.SerializeToString,
            auth__pb2.UsersDataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SetUserRole(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/AuthNotify/SetUserRole",
            auth__pb2.ChangeRoleRequest.SerializeToString,
            auth__pb2.ChangeRoleResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
