import stripe
from fastapi import APIRouter, status, Request, Header, Body
from uuid import UUID
from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from core.config import get_settings

config = get_settings()
router = APIRouter()
templates = Jinja2Templates(directory='templates')

stripe.api_key = config.STRIPE_SECRET_KEY


@router.get('/payment')
def payment():
    """Метод для создания customer (плательщика), создания сессии клиента.

    Принимает: JWT-token клиента
    Возвращает: Перенаправляет пользователя на страницу оплаты
    """
    user_id = 1
    customer = stripe.Customer.create(
        metadata={'user_id': user_id},
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
        success_url=config.success_page_url,
        cancel_url=config.cancel_page_url,
    )
    return RedirectResponse(session.url)


@router.get('/success', response_class=HTMLResponse)
async def success_page(request: Request):
    """Метод для возвращения шаблона успешной страницы оплаты

    Принимает: request: Request
    Возвращает: шаблон успешной страницы оплаты: html
    """
    return templates.TemplateResponse('success.html', {'request': request})


# @router.get('/cancel', response_class=HTMLResponse)
# async def cancel_page(request: Request):
#     """Метод для возвращения шаблона неуспешной страницы оплаты
#
#     Принимает: request: Request
#     Возвращает: шаблон неуспешной страницы оплаты: html
#     """
#     return templates.TemplateResponse('cancel.html', {'request': request})


@router.post(
    path='/webhook',
    status_code=status.HTTP_200_OK
)
async def webhook(
        request: Request,
        stripe_signature: str | None = Header(default=None)
):
    """
    Метод для работы с webhook stripe.

    params:
        request: Request - POST запрос от stripe
        stripe_signature: str - Данные с подписью stripe
    return:
        event: Event - событие stripe
    """
    event = None
    payload = await request.body()
    sig_header = stripe_signature
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, config.endpoint_secret
        )
    except ValueError as e:
        raise e
    except stripe.error.SignatureVerificationError as e:
        raise e
    if event['type'] == 'checkout.session.completed':
        payment_intent = event['data']['object']
    else:
        print('Unhandled event type {}'.format(event['type']))
    return


def get_user_id(stripe_customer_id: str) -> UUID:
    """Получает id пользователя по id пользователя в stripe.

    params: stripe_customer_id: string - id пользователя в stripe
    return: id: uuid - uuid пользователя
    """
    return stripe.Customer.retrieve(
        stripe_customer_id
    ).get('metadata').get('user_id')


def refund_payment(payment_intent: str) -> None:
    """Возвращает деньги пользователю.

    params:
        payment_intent: str - идентификатор платежа, который необходимо вернуть

    return: None
    """
    return stripe.Refund.create(
        payment_intent=payment_intent
    )
