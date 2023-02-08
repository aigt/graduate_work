import logging

from fastapi import APIRouter, Depends, status
from fastapi.responses import RedirectResponse

from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.aggregates_model.user_aggregate.user import User
from domain.services.payment_system import PaymentSystem
from web_api.configs.settings import Settings
from web_api.dependencies.common import get_settings
from web_api.dependencies.domain import get_user
from web_api.dependencies.infrastructure import (
    get_payment_repository,
    get_payment_system,
)

router = APIRouter()


@router.get("/pay_for_subscription", status_code=status.HTTP_200_OK)
async def pay_for_subscription(
    settings: Settings = Depends(get_settings),
    user: User = Depends(get_user),
    payment_system: PaymentSystem = Depends(get_payment_system),
    payment_repository: PaymentRepository = Depends(get_payment_repository),
) -> RedirectResponse:
    """Эндпоинт обработки запроса пользователя на оплату подписки.
    \f
    Args:
        settings (Settings): Depends(get_settings)
        user (User): Depends(get_user)
        payment_system (PaymentSystem): Depends(get_settings).
        payment_repository (PaymentRepository): Depends(get_payment_repository).

    Returns:
        RedirectResponse: Ссылка перенаправления со статусом 307.
    """
    payment = await user.pay_for_subscription(
        subscription_price=settings.subscription_price,
        payment_system=payment_system,
        payment_repository=payment_repository,
    )

    redirect_url = payment.confirm_url.id

    logging.info(
        "To confirm payment redirecting user {user_id} to url: {redirect_url}".format(
            user_id=user.id.id,
            redirect_url=redirect_url,
        ),
    )

    return RedirectResponse(redirect_url)
