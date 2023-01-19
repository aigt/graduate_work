from decimal import Decimal

from domain.aggregates_model.external_refund_aggregate.external_refund_amount import (
    ExternalRefundAmount,
)


class ExternalRefund:
    """Возврат зарегестрированный в платёжной системе."""

    id: str
    amount = ExternalRefundAmount()
    status: str
    payment_id: str

    def __init__(
        self,
        id: str,  # noqa: WPS125
        amount: Decimal,
        status: str,
        payment_id: str,
    ) -> None:
        self.id = id  # noqa: WPS601
        self.amount = amount  # noqa: WPS601
        self.status = status
        self.payment_id = payment_id
