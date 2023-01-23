from domain.aggregates_model.payment_aggregate.payment_amount import (
    PaymentAmount,
    PaymentAmountField,
)
from domain.aggregates_model.payment_aggregate.payment_external_body import (
    PaymentExternalBody,
    PaymentExternalBodyField,
)
from domain.aggregates_model.payment_aggregate.payment_external_id import (
    PaymentExternalId,
    PaymentExternalIdField,
)
from domain.aggregates_model.payment_aggregate.payment_id import (
    PaymentId,
    PaymentIdField,
)
from domain.aggregates_model.payment_aggregate.payment_refunded import (
    PaymentRefunded,
    PaymentRefundedField,
)
from domain.aggregates_model.payment_aggregate.payment_system_id import (
    PaymentSystemId,
    PaymentSystemIdField,
)
from domain.aggregates_model.payment_aggregate.payment_user_id import (
    PaymentUserId,
    PaymentUserIdField,
)


class Payment:
    """Платёж."""

    id: PaymentId = PaymentIdField()
    user_id: PaymentUserId = PaymentUserIdField()
    amount: PaymentAmount = PaymentAmountField()
    external_id: PaymentExternalId = PaymentExternalIdField()
    external_payment: PaymentExternalBody = PaymentExternalBodyField()
    refunded: PaymentRefunded = PaymentRefundedField()
    system_id: PaymentSystemId = PaymentSystemIdField()

    def __init__(
        self,
        id: PaymentUserId,  # noqa: WPS125
        user_id: PaymentUserId,
        amount: PaymentAmount,
        external_id: PaymentExternalId,
        external_payment: PaymentExternalBody,
        refunded: PaymentRefunded,
        system_id: PaymentSystemId,
    ) -> None:
        self.id = id  # noqa: WPS601
        self.user_id = user_id  # noqa: WPS601
        self.amount = amount  # noqa: WPS601
        self.external_id = external_id  # noqa: WPS601
        self.external_payment = external_payment  # noqa: WPS601
        self.refunded = refunded  # noqa: WPS601
        self.system_id = system_id  # noqa: WPS601
