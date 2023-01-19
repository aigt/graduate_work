from uuid import UUID


class Payment:
    """Платёж."""

    id: UUID
    user_id: UUID
    amount: UUID
    external_id: str
    external_payment: str
