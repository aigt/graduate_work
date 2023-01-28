from logging import config as logging_config


def configure_logging() -> None:
    """Конфигурировать логер."""
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # noqa: WPS323

    log_default_handlers = [
        "console",
    ]

    logging = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {"format": log_format},
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(levelprefix)s %(message)s",  # noqa: WPS323
                "use_colors": None,
            },
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": "%(levelprefix)s %(client_addr)s - '%(request_line)s' %(status_code)s",  # noqa: WPS323
            },
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            },
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "access": {
                "formatter": "access",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "": {
                "handlers": log_default_handlers,
                "level": "INFO",
            },
            "uvicorn.error": {
                "level": "INFO",
            },
            "uvicorn.access": {
                "handlers": ["access"],
                "level": "INFO",
                "propagate": False,
            },
        },
        "root": {
            "level": "DEBUG",
            "formatter": "verbose",
            "handlers": log_default_handlers,
        },
    }

    logging_config.dictConfig(logging)
