import stripe as stripe

from fastapi import Request

from domain.aggregates_model.external_payment_aggregate.external_payment import (
    ExternalPayment,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_amount import (
    ExternalPaymentAmount,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_id import (
    ExternalPaymentId,
)
from domain.aggregates_model.external_payment_aggregate.external_payment_status import ExternalPaymentStatusEnum
from domain.aggregates_model.external_refund_aggregate.external_refund import (
    ExternalRefund,
)
from domain.aggregates_model.external_refund_aggregate.external_refund_amount import (
    ExternalRefundAmount,
)
from domain.aggregates_model.external_refund_aggregate.external_refund_id import (
    ExternalRefundId,
)
from domain.aggregates_model.external_refund_aggregate.external_refund_payment_id import (
    ExternalRefundPaymentId,
)
from domain.services.payment_system import PaymentSystem


from infrastructure.payment_system.core.config import get_settings

config = get_settings()

stripe.api_key = config.STRIPE_SECRET_KEY


class StripePaymentSystem(PaymentSystem):
    """Платёжная система Stripe.

    Документация по API внешнего сервиса доступна по ссылке:
    https://stripe.com/docs/api
    """

    @property
    async def system_id(self) -> str:
        """Идентификатор платёжной системы.

        Returns:
            str: Идентификатор.
        """
        return "stripe"

    async def create_payment(self, amount: ExternalPaymentAmount) -> ExternalPayment:
        """Создать платёж.

        Args:
            amount (ExternalPaymentAmount): Сумма платежа.

        Returns:
            ExternalPayment: Созданный платёж.
        """
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': amount,
                    'product_data': {
                        'name': 'Subscription',
                        'description': '',
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=config.success_page_url,
            cancel_url=config.cancel_page_url,
        )
        return ExternalPayment(
            id=session.id,
            amount=session.amount_total,
            status=ExternalPaymentStatusEnum.PENDING,
            confirm_url=session.url
        )

    async def payments(self) -> list[ExternalPayment]:
        """Получить список платежей зарегистрированных в платёжной системе.

        Returns:
            list[ExternalPayment]: Список платежей в актуальном состоянии.
        """
        list_payments = []
        payments = stripe.PaymentIntent.list(limit=100)
        for payment in payments.auto_paging_iter():
            payment_obj = ExternalPayment(
                id=payment.id,
                amount=payment.amount,
                status=payment.status,
                confirm_url='',
            )
            list_payments.append(payment_obj)
        return list_payments

    async def payment_by_id(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Получить информацию о платеже в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе в актуальном состоянии.
        """
        payment = stripe.PaymentIntent.retrieve(payment_id)
        return ExternalPayment(
            id=payment.id,
            amount=payment.amount,
            status=payment.status,
            confirm_url='',
        )

    async def capture_payment(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Подтвердить платёж в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе в актуальном состоянии.
        """
        return NotImplemented

    async def cancel_payment(self, payment_id: ExternalPaymentId) -> ExternalPayment:
        """Отменить платёж в платёжной системе.

        Args:
            payment_id (ExternalPaymentId): Идентификатор платежа.

        Returns:
            ExternalPayment: Платёж в системе в актуальном состоянии.
        """
        return NotImplemented

    async def refunds(self) -> list[ExternalRefund]:
        """Получить список возвратов зарегестрированных в платёжной системе.

        Returns:
            list[ExternalRefund]: Список возвратов в актуальном состоянии.
        """
        return NotImplemented

    async def create_refund(self, amount: ExternalRefundAmount, payment_id: ExternalRefundPaymentId) -> ExternalRefund:
        """Создать возврат.

        Args:
            amount (ExternalRefundAmount): Сумма возврата.
            payment_id (ExternalRefundPaymentId): Идентификатор платежа, на который осуществляется возврат.

        Returns:
            ExternalRefund: Созданный возврат.
        """
        refund = stripe.Refund.create(payment_intent=payment_id, amount=amount)
        return ExternalRefund(
            id=refund.id,
            amount=refund.amount,
            status=refund.status,
            payment_id=refund.payment_intent
        )

    async def refund_by_id(self, refund_id: ExternalRefundId) -> ExternalRefund:
        """Получить информацию о возврате в платёжной системе.

        Args:
            refund_id (ExternalRefundId): Идентификатор возврата.

        Returns:
            ExternalRefund: Возврат в системе в актуальном состоянии.
        """
        refund_info = stripe.Refund.retrieve(refund_id)
        return ExternalRefund(
            id=refund_info.id,
            amount=refund_info.amount,
            status=refund_info.status,
            payment_id=refund_info.payment_intent
        )

    async def webhook(
            request: Request,
            stripe_signature: str
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
