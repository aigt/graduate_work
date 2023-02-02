from typing import Generator

import psycopg
from psycopg.rows import dict_row
from pytest import fixture
from settings import get_settings

settings = get_settings()


@fixture(scope="function")
def postgres_cur() -> Generator:
    """Postgres курсор.

    Yields:
        cur(Generator): Postgres курсор.
    """
    con = psycopg.connect(
        host=settings.postgres_users_host,
        port=settings.postgres_port,
        dbname=settings.payments_db,
        user=settings.postgres_user,
        password=settings.postgres_password,
        row_factory=dict_row,
    )
    cur = con.cursor()
    yield cur
    con.close()
