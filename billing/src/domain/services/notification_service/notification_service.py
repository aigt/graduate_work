import logging
from abc import ABC, abstractmethod
from http import HTTPStatus

import aiohttp

from domain.aggregates_model.external_refund_aggregate.external_refund_amount import (
    ExternalRefundAmount,
)
from domain.aggregates_model.user_aggregate.user_id import UserId
from domain.services.notification_service.request_model import (
    Meta,
    Notification,
    NotificationScale,
    NotificationType,
    NotificationUrgency,
)

logger = logging.getLogger(__name__)


class NotificationService(ABC):
    """Сервис оповещений."""

    @abstractmethod
    async def notify_user_about_payment(self, user_id: UserId) -> None:
        """Оповестить пользователя о платеже.

        Args:
            user_id (UserId): Id пользователя.
        """

    @abstractmethod
    async def notify_user_about_refund(self, user_id: UserId, amount: ExternalRefundAmount) -> None:
        """Оповестить пользователя о возврате.

        Args:
            user_id (UserId): Id пользователя.
            amount (ExternalRefundAmount): Сумма возврата.
        """


class Notifications(NotificationService):
    """Сервис для работы с сервисом оповещений."""

    def __init__(self, url_notification_service: str):
        self.url = url_notification_service

    async def notify_user_about_payment(self, user_id: UserId) -> None:
        """Оповестить пользователя о платеже.

        Args:
            user_id (UserId): Id пользователя.
        """
        await self._send({"user_id": user_id})

    async def notify_user_about_refund(self, user_id: UserId, amount: ExternalRefundAmount) -> None:
        """Оповестить пользователя о возврате.

        Args:
            user_id (UserId): Id пользователя.
            amount (ExternalRefundAmount): Сумма возврата.
        """
        data_for_send = {"user_id": user_id, "amount": amount}
        await self._send(data_for_send)

    async def _send(self, data_for_send: dict) -> None:
        """Отправка запроса об уведомлении.

        Args:
            data_for_send(dict): Данные помещаемые в поле fields

        Return: None
        """
        body = Notification(
            meta=Meta(urgency=NotificationUrgency.immediate, scale=NotificationScale.individual, periodic=False),
            type=NotificationType.info,
            fields=data_for_send,
        ).dict()

        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=body) as response:
                if response.status == HTTPStatus.OK:
                    logger.info("Notification request - sent")
                    return
        user_id = data_for_send.get("user_id")
        logger.warning(f"Notification reqeust for {user_id} dont sent")
