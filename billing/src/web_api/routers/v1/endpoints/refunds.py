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
from web_api.routers.v1.schemas.errors import ErrorResponse
from web_api.routers.v1.schemas.responses import SimpleResponse

router = APIRouter()


@router.get(
    "/refund_subscription",
    status_code=status.HTTP_200_OK,
    response_model=SimpleResponse,
    responses={status.HTTP_403_FORBIDDEN: {"model": ErrorResponse}},
    summary="Вернуть деньги за подписку.",
)
async def refund_subscription(
    user: User = Depends(get_user),
    payment_system: PaymentSystem = Depends(get_payment_system),
    payment_repository: PaymentRepository = Depends(get_payment_repository),
) -> SimpleResponse:
    """Эндпоинт обработки запроса пользователя на отмену подписки.
    \f
    Args:
        user (User): Depends(get_user)
        payment_system (PaymentSystem): Depends(get_settings).
        payment_repository (PaymentRepository): Depends(get_payment_repository).

    Returns:
        SimpleResponse: Ответ.
    """
    await user.refund_subscription(
        payment_system=payment_system,
        payment_repository=payment_repository,
    )
    return SimpleResponse(message="Payment successfully refunded.")
