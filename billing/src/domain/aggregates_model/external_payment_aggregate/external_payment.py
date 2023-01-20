from decimal import Decimal


class ExternalPayment:
    """Платёж зарегестрированный в платёжной системе."""

    id: str
    amount: Decimal
    status: str
    confirm_url: str
