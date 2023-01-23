import stripe
from fastapi import APIRouter
from requests import Response

from core.config import get_settings

config = get_settings()

router = APIRouter()
from pydantic import BaseModel


class Film(BaseModel):
    status: str


@router.get('/payment', response_model=Film)
async def test_payment():
    stripe.api_key = config.STRIPE_SECRET_KEY
    data = {
        "name": 'Subscription',
        "quantity": 1,
        "currency": 'usd',
        "amount": 1,
    }
    checkout_session = stripe.checkout.Session.create(
        success_url='http://127.0.0.1:8000/success',
        cancel_url='http://127.0.0.1:8000/cancel',
        line_items=[
            data,
        ],
        mode="payment",
    )
    return Film(status=checkout_session.status_code)
