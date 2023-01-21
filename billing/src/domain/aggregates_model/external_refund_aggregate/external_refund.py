from domain.aggregates_model.external_refund_aggregate.external_refund_amount import (
    ExternalRefundAmount,
    ExternalRefundAmountField,
)
from domain.aggregates_model.external_refund_aggregate.external_refund_id import (
    ExternalRefundId,
    ExternalRefundIdField,
)
from domain.aggregates_model.external_refund_aggregate.external_refund_payment_id import (
    ExternalRefundPaymentId,
    ExternalRefundPaymentIdField,
)
from domain.aggregates_model.external_refund_aggregate.external_refund_status import (
    ExternalRefundStatus,
    ExternalRefundStatusField,
)


class ExternalRefund:
    """Возврат зарегестрированный в платёжной системе."""

    id: ExternalRefundId = ExternalRefundIdField()
    amount: ExternalRefundAmount = ExternalRefundAmountField()
    status: ExternalRefundStatus = ExternalRefundStatusField()
    payment_id: ExternalRefundPaymentId = ExternalRefundPaymentIdField()

    def __init__(
        self,
        id: ExternalRefundId,  # noqa: WPS125
        amount: ExternalRefundAmount,
        status: ExternalRefundStatus,
        payment_id: ExternalRefundPaymentId,
    ) -> None:
        self.id = id  # noqa: WPS601
        self.amount = amount  # noqa: WPS601
        self.status = status  # noqa: WPS601
        self.payment_id = payment_id  # noqa: WPS601
