from logging import getLogger

import backoff
import psycopg
from core.logger import configure_logging
from core.settings import get_settings
from psycopg import connect

from src.external_services.auth_service.authorization_service import (
    AuthorizationService,
)
from src.external_services.notification_service.notification_service import (
    NotificationService,
)
from src.repositories.postgres import PostgresRepository
from src.scheduler import Scheduler

settings = get_settings()


@backoff.on_exception(backoff.expo, psycopg.OperationalError)
def main() -> None:
    """Старт процесса."""
    configure_logging()
    getLogger(__name__).info("Scheduler run")
    con = connect(
        host=settings.postgres_host,
        port=settings.postgres_port,
        dbname=settings.postgres_db,
        user=settings.postgres_user,
        password=settings.postgres_password,
    )
    notification = NotificationService(settings.notification_url)
    auth = AuthorizationService(settings.authorization_grpc_address)
    repo = PostgresRepository(con)
    scheduler = Scheduler(repo, notification, auth)
    scheduler.run(settings.interval)


if __name__ == "__main__":
    main()
