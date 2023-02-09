#!/bin/bash

cd /opt/app/

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --no-input --clear

export DJANGO_SUPERUSER_EMAIL
export DJANGO_SUPERUSER_PASSWORD
export DJANGO_SUPERUSER_LOGIN

python manage.py createsuperuser --username ${DJANGO_SUPERUSER_LOGIN}  --noinput

uwsgi --strict --ini uwsgi.ini

exec "$@"
