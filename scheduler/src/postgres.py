import datetime
from datetime import timedelta
from logging import getLogger

from psycopg import Connection
from psycopg.rows import dict_row


class PostgresRepository:
    """Работа с Постгрес."""

    def __init__(self, con: Connection):
        self.con = con

    def update_expired_subscribe_users(self) -> None:
        """Изменение статусов подписки в зависимости от времени."""
        current_time = datetime.datetime.now()
        expired = current_time - timedelta(days=30)
        sql = """
        UPDATE payments.subscribers
        SET subscriber_status = false
        WHERE subscribers.date_subscribe < %s AND subscribers.subscriber_status = true
        """
        with self.con.cursor(row_factory=dict_row) as cur:
            cur.execute(sql, (expired,))
            getLogger(__name__).info(cur.statusmessage)
            self.con.commit()
