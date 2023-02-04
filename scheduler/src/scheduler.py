import time
from logging import getLogger

from src.external_services.auth_service.authorization_service import (
    AuthorizationService,
)
from src.external_services.notification_service.notification_service import (
    NotificationService,
)
from src.repositories.postgres import PostgresRepository


class Scheduler:
    """Процесс периодической проверки статусов подписчиков."""

    def __init__(
        self,
        repository: PostgresRepository,
        notification_service: NotificationService,
        authorization_service: AuthorizationService,
    ):
        self.repo = repository
        self.notification = notification_service
        self.authorization = authorization_service

    def run(self, interval: int) -> None:
        """Запуск проверки статусов с интервалом.

        Args:
            interval(int): Промежуток между проверками в секундах.
        """
        while True:
            for users in self.repo.get_expired_subscribe_users():
                ids = [str(user.get("user_id")) for user in users]
                self.notification.end_subscription_notification(ids)
                for user_id in ids:
                    self.authorization.del_subscriber_status(user_id)
            self.repo.update_expired_subscribe_users()
            getLogger(__name__).info(f"After update - sleep {interval} seconds")
            time.sleep(interval)
