"""Модуль для работы с PostgreSQL."""
import logging
from typing import Optional

import backoff
import psycopg
from psycopg import AsyncConnection


class PostgresDB:
    """Класс для работы с базой Postgres."""

    def __init__(self, postgres_dsn: str) -> None:
        self._postgres_dsn = postgres_dsn
        self._connection: Optional[AsyncConnection] = None

    @backoff.on_exception(backoff.expo, psycopg.Error)
    async def init_connection(self) -> None:
        """Инициализировать соединение с БД."""
        logging.info("Initializing connection to PostgreSQL")

        self._connection = await psycopg.AsyncConnection.connect(conninfo=self._postgres_dsn)

    @property
    def connection(self) -> AsyncConnection:
        """Клиент PostgresDB.

        Raises:
            Exception: Соединение не инициализировано.

        Returns:
            AsyncConnection: Соединение с Postgres
        """
        if self._connection is None:
            raise Exception("PostgresDBConnectionIsNotInitializedError")  # noqa: WPS454
        return self._connection

    async def close_connection(self) -> None:
        """Закрыть соединение с БД.

        Raises:
            Exception: Соединение не инициализировано.
        """
        logging.info("Closing PostgreSQL connection")

        if self._connection is None:
            raise Exception("PostgresDBConnectionIsNotInitializedError")  # noqa: WPS454
        await self._connection.close()
