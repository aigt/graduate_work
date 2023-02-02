from fastapi import Depends

from domain.aggregates_model.payment_aggregate.payment_reposytory import (
    PaymentRepository,
)
from domain.services.auth_service import AuthService
from domain.services.notification_service import NotificationService
from domain.services.payment_system import PaymentSystem
from infrastructure.auth_service.movie_auth_service import MovieAuthService
from infrastructure.notification_system.movie_notification_system import (
    MovieNotificationService,
)
from infrastructure.payment_repository.payment_reposytory import (
    PostgresPaymentRepository,
)
from infrastructure.payment_system.stripe_payment_system import StripePaymentSystem
from web_api.configs.settings import Settings
from web_api.dependencies.common import get_settings


def get_payment_repository() -> PaymentRepository:
    """Фабрика репозиториев платежей.

    Returns:
        PaymentRepository: Репозиторий платежей.
    """
    return PostgresPaymentRepository()


def get_notification_service() -> NotificationService:
    """Фабрика нотификационных сервисов.

    Returns:
        NotificationService: Нотификационный сервис.
    """
    return MovieNotificationService()


def get_auth_service(settings: Settings = Depends(get_settings)) -> AuthService:
    """Фабрика сервиса авторизации.

    Args:
        settings (Settings): Depends(get_settings).

    Returns:
        AuthService: Сервис авторизации.
    """
    return MovieAuthService(host=settings.auth_service_host)


def get_payment_system(
    payment_repository: PaymentRepository = Depends(get_payment_repository),
    notification_service: AuthService = Depends(get_notification_service),
    auth_service: AuthService = Depends(get_auth_service),
) -> PaymentSystem:
    """Фабрика платёжных систем.

    Args:
        payment_repository (PaymentRepository): Depends(get_payment_repository).
        notification_service (AuthService): Depends(get_notification_service).
        auth_service (AuthService): Depends(get_auth_service).

    Returns:
        PaymentSystem: Платёжная система.
    """
    return StripePaymentSystem(
        payment_repository=payment_repository,
        auth_service=auth_service,
        notification_service=notification_service,
    )