#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main() -> None:
    """Run administrative tasks."""  # noqa: DAR401
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line  # noqa: WPS433
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "  # noqa: WPS326
            "forget to activate a virtual environment?"  # noqa: WPS326, C812
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
