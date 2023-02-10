import logging
import os

from cachetools import cached  # type: ignore
from cachetools.keys import hashkey  # type: ignore
from fastapi import Depends
from psycopg import AsyncConnection

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
from web_api.dependencies.db import get_postgres_connection


@cached(
    cache={},
    key=lambda connection: hashkey("PaymentRepository"),
)
def get_payment_repository(connection: AsyncConnection = Depends(get_postgres_connection)) -> PaymentRepository:
    """Фабрика репозиториев платежей.

    Args:
        connection (AsyncConnection): Depends(get_postgres_connection).

    Returns:
        PaymentRepository: Репозиторий платежей.
    """
    logging.info("Creating and caching PaymentRepository, pid: {pid}".format(pid=os.getpid()))

    return PostgresPaymentRepository(connect=connection)


@cached(
    cache={},
    key=lambda settings: hashkey("NotificationService"),
)
def get_notification_service(settings: Settings = Depends(get_settings)) -> NotificationService:
    """Фабрика нотификационных сервисов.

    Args:
        settings (Settings): Depends(get_settings).

    Returns:
        NotificationService: Нотификационный сервис.
    """
    logging.info("Creating and caching NotificationService, pid: {pid}".format(pid=os.getpid()))
    return MovieNotificationService(settings.notification_service_host)


@cached(
    cache={},
    key=lambda settings: hashkey("AuthService"),
)
def get_auth_service(settings: Settings = Depends(get_settings)) -> AuthService:
    """Фабрика сервиса авторизации.

    Args:
        settings (Settings): Depends(get_settings).

    Returns:
        AuthService: Сервис авторизации.
    """
    logging.info("Creating and caching AuthService, pid: {pid}".format(pid=os.getpid()))
    return MovieAuthService(host=settings.auth_service_host)


@cached(
    cache={},
    key=lambda payment_repository, notification_service, auth_service, settings: hashkey("PaymentSystem"),
)
def get_payment_system(
    payment_repository: PaymentRepository = Depends(get_payment_repository),
    notification_service: AuthService = Depends(get_notification_service),
    auth_service: AuthService = Depends(get_auth_service),
    settings: Settings = Depends(get_settings),
) -> PaymentSystem:
    """Фабрика платёжных систем.

    Args:
        payment_repository (PaymentRepository): Depends(get_payment_repository).
        notification_service (AuthService): Depends(get_notification_service).
        auth_service (AuthService): Depends(get_auth_service).
        settings (Settings): Depends(get_settings).

    Returns:
        PaymentSystem: Платёжная система.
    """
    logging.info("Creating and caching PaymentSystem, pid: {pid}".format(pid=os.getpid()))

    return StripePaymentSystem(
        payment_repository=payment_repository,
        auth_service=auth_service,
        notification_service=notification_service,
        success_url=settings.stripe_success_url,
        cancel_url=settings.stripe_cancel_url,
        stripe_secret_key=settings.stripe_secret_key,
        limit=settings.stripe_limit_per_page,
    )
