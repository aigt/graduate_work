from domain.aggregates_model.external_payment_aggregate.external_payment_amount import (
    ExternalPaymentAmount,
    ExternalPaymentAmountField,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_confirm_url import (
    ExternalPaymentConfirmUrl,
    ExternalPaymentConfirmUrlField,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_id import (
    ExternalPaymentId,
    ExternalPaymentIdField,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_status import (
    ExternalPaymentStatus,
    ExternalPaymentStatusField,
)


class ExternalPayment:
    """Платёж зарегестрированный в платёжной системе."""

    id: ExternalPaymentId = ExternalPaymentIdField()
    amount: ExternalPaymentAmount = ExternalPaymentAmountField()
    status: ExternalPaymentStatus = ExternalPaymentStatusField()
    confirm_url: ExternalPaymentConfirmUrl = ExternalPaymentConfirmUrlField()

    def __init__(
        self,
        id: ExternalPaymentId,  # noqa: WPS125
        amount: ExternalPaymentAmount,
        status: ExternalPaymentStatus,
        confirm_url: ExternalPaymentConfirmUrl,
    ) -> None:
        self.id = id  # noqa: WPS601
        self.amount = amount  # noqa: WPS601
        self.status = status  # noqa: WPS601
        self.confirm_url = confirm_url  # noqa: WPS601
