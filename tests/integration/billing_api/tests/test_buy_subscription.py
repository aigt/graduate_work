from http import HTTPStatus

from psycopg import Cursor
from requests import Session  # type: ignore
from settings import get_settings
from testdata.user_id import user_id
from utils.get_jwt import get_token

settings = get_settings()


def test_buy(postgres_cur: Cursor, http_con: Session) -> None:
    """Тест успешной покупки подписки.

    Args:
        postgres_cur(Cursor): Курсор постгреса
        http_con(Session): http сессия
    """
    token = get_token(user_id)
    response = http_con.get(
        url=f"{settings.url}/payments/pay_for_subscription",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == HTTPStatus.OK


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
