import os

DATABASES = {  # noqa: WPS407
    "default": {
        "ENGINE": os.environ.get("POSTGRES_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("POSTGRES_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
        "OPTIONS": {"options": "-c search_path=public,payments"},
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
