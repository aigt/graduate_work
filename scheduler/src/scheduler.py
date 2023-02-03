import time
from logging import getLogger

from src.postgres import PostgresRepository


class Scheduler:
    """Процесс периодической проверки статусов подписчиков."""

    def __init__(self, repository: PostgresRepository):
        self.repo = repository

    def run(self, interval: int) -> None:
        """Запуск проверки статусов с интервалом.

        Args:
            interval(int): Промежуток между проверками в секундах.
        """
        while True:
            self.repo.update_expired_subscribe_users()
            getLogger(__name__).info(f"After update - sleep {interval} seconds")
            time.sleep(interval)
