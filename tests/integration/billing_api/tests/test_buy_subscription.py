from http import HTTPStatus

from psycopg import Cursor
from requests import Session  # type: ignore
from settings import get_settings

settings = get_settings()


def test_buy(postgres_cur: Cursor, http_con: Session) -> None:
    """Тест успешной покупки подписки.

    Args:
        postgres_cur(Cursor): Курсор постгреса
        http_con(Session): http сессия
    """


def test_buy_unauthorized(http_con: Session) -> None:
    """Тест доступа к ендпоинту для покупки подписки.

    Args:
        http_con(Session): http сессия
    """
    body = None
    response = http_con.get(
        f"{settings.url}/payments/pay_for_subscription",
        json=body,
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
