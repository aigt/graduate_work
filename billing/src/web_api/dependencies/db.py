from psycopg import AsyncConnection

from infrastructure.db.postgres import PostgresDB

postgres: PostgresDB | None


async def get_postgres_connection() -> AsyncConnection:
    """Фабрика подключений PostgreSQL.

    Returns:
        AsyncConnection: Подключение.

    Raises:
        Exception: Соединение не инициализировано.
    """
    if postgres is None:  # noqa: F821
        raise Exception("PostgresDBConnectionIsNotInitializedError")  # noqa: WPS454
    return postgres.connection  # noqa: F821
