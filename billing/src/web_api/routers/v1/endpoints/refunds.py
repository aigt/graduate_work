from fastapi import APIRouter, Depends, status

from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.aggregates_model.user_aggregate.user import User
from domain.services.payment_system import PaymentSystem
from web_api.dependencies.domain import get_user
from web_api.dependencies.infrastructure import (
    get_payment_repository,
    get_payment_system,
)

router = APIRouter()


@router.get("/refund_subscription", status_code=status.HTTP_200_OK)
async def refund_subscription(
    user: User = Depends(get_user),
    payment_system: PaymentSystem = Depends(get_payment_system),
    payment_repository: PaymentRepository = Depends(get_payment_repository),
) -> status.HTTP_200_OK:
    """Эндпоинт обработки запроса пользователя на отмену подписки.
    \f
    Args:
        user (User): Depends(get_user)
        payment_system (PaymentSystem): Depends(get_settings).
        payment_repository (PaymentRepository): Depends(get_payment_repository).

    Returns:
        RedirectResponse: Ссылка перенаправления со статусом 307.
    """
    await user.refund_subscription(
        payment_system=payment_system,
        payment_repository=payment_repository,
    )
