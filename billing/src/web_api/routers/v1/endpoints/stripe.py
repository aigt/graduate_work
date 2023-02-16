import logging

import stripe
from fastapi import APIRouter, Depends, Header, Request, status

from domain.aggregates_model.external_payment_aggregate.external_payment_status import (
    ExternalPaymentStatus,
    ExternalPaymentStatusEnum,
)
from domain.aggregates_model.payment_aggregate.payment_id import PaymentId
from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.aggregates_model.payment_aggregate.session_id import SessionId
from domain.services.payment_system import PaymentSystem
from infrastructure.payment_system.stripe_payment_system import (
    ExternalPaymentStatusStripeEnum,
)
from web_api.configs.settings import Settings
from web_api.dependencies.common import get_settings
from web_api.dependencies.infrastructure import (
    get_payment_repository,
    get_payment_system,
)
from web_api.routers.v1.schemas.errors import ErrorResponse
from web_api.routers.v1.schemas.responses import StripeCallbackResponse

router = APIRouter()


@router.post(
    "/callback",
    status_code=status.HTTP_200_OK,
    response_model=StripeCallbackResponse,
    responses={status.HTTP_403_FORBIDDEN: {"model": ErrorResponse}},
    summary="Вэбхук stripe.",
)
async def callback(
    request: Request,
    settings: Settings = Depends(get_settings),
    payment_repository: PaymentRepository = Depends(get_payment_repository),
    stripe_signature: str | None = Header(default=None),
    payment_system: PaymentSystem = Depends(get_payment_system),
) -> StripeCallbackResponse:
    """Эндпоинт обратного вызова для вэбхука stripe.

    Более подробную информацию о приходящих запросах - см.:

    - Events object: <https://stripe.com/docs/api/events/object>
    - Webhooks: <https://stripe.com/docs/webhooks#acknowledge-events-immediately>
    \f
    Args:
        request (Request): Request.
        settings (Settings): Depends(get_settings)
        payment_repository (PaymentRepository): Репозторий платежей
        stripe_signature (Header): Stripe signature
        payment_system (PaymentSystem): Depends(get_payment_system)

    Raises:
        ValueError: Некорректный пэйлод.
        invalid_signature_exception: Некорректная сигнатура.

    Returns:
        StripeCallbackResponse: Отклик со статусом 200.
    """
    event = None
    payload = await request.body()
    sig_header = stripe_signature

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.endpoint_secret,
        )
    except ValueError as invalid_payload_exception:  # noqa:WPS329
        raise invalid_payload_exception
    except stripe.error.SignatureVerificationError as invalid_signature_exception:  # noqa:WPS329
        raise invalid_signature_exception

    if event["type"] == "checkout.session.completed":
        session_id = SessionId(event["data"]["object"]["id"])
        payment_intent = PaymentId(event["data"]["object"]["payment_intent"])
        if event["data"]["object"]["payment_status"] == ExternalPaymentStatusStripeEnum.PAID.value:
            payment_status = ExternalPaymentStatus(status=ExternalPaymentStatusEnum.SUCCEDED.value)
        else:
            payment_status = ExternalPaymentStatus(status=ExternalPaymentStatusEnum.CANCELED.value)
        await payment_repository.set_payment_id_by_payment_system(
            session_id,
            payment_intent,
            payment_status,
        )
    else:
        logging.info("Unhandled event type {}".format(event["type"]))

    return StripeCallbackResponse(success="True")
