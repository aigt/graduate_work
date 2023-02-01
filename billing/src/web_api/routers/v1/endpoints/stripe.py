import logging

import stripe
from fastapi import APIRouter, Depends, Request, status

from domain.services.payment_system import PaymentSystem
from web_api.configs.settings import Settings
from web_api.dependencies.common import get_settings
from web_api.dependencies.infrastructure import get_payment_system

router = APIRouter()


@router.post("/callback", status_code=status.HTTP_200_OK)
async def callback(
    request: Request,
    settings: Settings = Depends(get_settings),
    payment_system: PaymentSystem = Depends(get_payment_system),
) -> dict[str, str]:
    """Эндпоинт обратного вызова для вэбхука.

    Events object: https://stripe.com/docs/api/events/object
    Webhooks: https://stripe.com/docs/webhooks#acknowledge-events-immediately
    \f
    Args:
        request (Request): Request.
        settings (Settings): Depends(get_settings).
        payment_system (PaymentSystem): Depends(get_payment_system).

    Raises:
        ValueError: Некорректный пэйлод.
        invalid_signature_exception: Некорректная сигнатура.

    Returns:
        dict[str, str]: Отклик со статусом 200.
    """
    event: stripe.Event | None = None
    payload = await request.body()
    sig_header = request.headers.get("STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.endpoint_secret)
    except ValueError as invalid_payload_exception:  # noqa:WPS329
        # Invalid payload
        raise invalid_payload_exception
    except stripe.error.SignatureVerificationError as invalid_signature_exception:  # noqa:WPS329
        # Invalid signature
        raise invalid_signature_exception

    # Handle the event type
    event_type = event["type"]
    logging.info("Handled event type {event_type}".format(event_type=event_type))

    # Здесь нужно вытащить payment_intent
    # https://stripe.com/docs/api/checkout/sessions/object#checkout_session_object-payment_intent
    payment_intent = event["... object ..."]["... payment_intent ..."]

    payment_system.on_payment_event(id=payment_intent, event=event_type)

    return {"success": "True"}
