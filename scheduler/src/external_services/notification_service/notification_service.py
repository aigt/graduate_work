from http import HTTPStatus
from logging import getLogger
from typing import List

from requests import post  # type: ignore

from src.external_services.notification_service.requests_model import (
    Meta,
    Notification,
    NotificationScale,
    NotificationType,
    NotificationUrgency,
)


class NotificationService:
    """Интерфейс работы с сервисом уведомлений."""

    def __init__(self, url_notification_service: str):
        self.url = url_notification_service

    def end_subscription_notification(self, user_id: str | List[str]) -> None:
        """Отправка уведомления об окончании подписочного периода.

        Args:
            user_id(str): Идентификатор пользователя.
        """
        body = Notification(
            meta=Meta(urgency=NotificationUrgency.immediate, scale=NotificationScale.individual, periodic=False),
            type=NotificationType.info,
            fields={"user_id": user_id},
        ).dict()

        response = post(url=self.url, json=body)
        if response.status_code == HTTPStatus.OK:
            getLogger(__name__).info("Notification request - sent")
            return
        getLogger(__name__).warning(f"Notification reqeust for {user_id} dont sent")
