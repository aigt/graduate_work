from decimal import Decimal


class ExternalRefund:
    """Возврат зарегестрированный в платёжной системе."""

    id: str
    amount: Decimal
    status: str
    payment_id: str
