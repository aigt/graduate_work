import logging

import stripe
from fastapi import APIRouter, Depends, Request, status

from web_api.configs.settings import Settings
from web_api.dependencies.common import get_settings

router = APIRouter()


@router.post("/callback", status_code=status.HTTP_200_OK)
async def callback(
    request: Request,
    settings: Settings = Depends(get_settings),
) -> dict[str, str]:
    """Эндпоинт обратного вызова для вэбхука.
    \f
    Args:
        request (Request): _description_
        settings (Settings): _description_. Defaults to Depends(get_settings).

    Raises:
        ValueError: Некорректный пэйлоад.
        invalid_signature_exception: Некорректная сигнатура.

    Returns:
        dict[str, str]: Отклик со статусом 200.
    """
    event = None
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

    # Handle the event
    logging.info("Handled event type {event_type}".format(event_type=event["type"]))

    return {"success": "True"}
