import os

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

ROOT_URLCONF = "admin_panel.urls"

WSGI_APPLICATION = "admin_panel.wsgi.application"
