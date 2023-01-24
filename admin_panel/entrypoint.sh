#!/bin/bash

cd /opt/app/

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --no-input --clear

uwsgi --strict --ini uwsgi.ini

exec "$@"
