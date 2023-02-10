from typing import Any

from psycopg import Cursor


def get_payment_info(cursor: Cursor, user_id: str) -> Any:
    """Получение данных об оплате подписки.

    Args:
        cursor(Cursor): Курсор базы данных.
        user_id(str): Идентификатор пользователя

    Returns:
        payment_info(Any)
    """
    sql = """
    SELECT external_payment, refunded
    FROM payments.payments
    WHERE user_id = %s
    """
    cursor.execute(sql, (user_id,))
    return cursor.fetchone()
