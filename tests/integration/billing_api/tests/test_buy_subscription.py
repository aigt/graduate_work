from psycopg import Cursor
from requests import Session  # type: ignore


def test_buy(postgres_cur: Cursor, http_con: Session) -> None:
    """Тест успешной покупки подписки.

    Args:
        postgres_cur(Cursor): Курсор постгреса
        http_con(Session): http сессия
    """
