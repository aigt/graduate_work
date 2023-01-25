import stripe
from fastapi import APIRouter
from starlette.responses import RedirectResponse
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from core.config import get_settings

config = get_settings()
router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get('/payment')
def payment():
    user_id = 1
    stripe.api_key = config.STRIPE_SECRET_KEY
    customer = stripe.Customer.create(
        metadata={'id': user_id},
    )
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': 1000,
                'product_data': {
                    'name': 'Subscription',
                    'description': 'alexit@ya.ru',
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        customer=customer.id,
        success_url='http://0.0.0.0:8000/api/v1/success',
        cancel_url='https://example.com/cancel',
    )
    return RedirectResponse(session.url)


@router.get("/success", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("success.html", {"request": request})


@router.get('/payment')
def payment():
    user_id = 1
    stripe.api_key = config.STRIPE_SECRET_KEY

    return RedirectResponse(session.url)
