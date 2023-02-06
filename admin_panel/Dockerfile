FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

COPY requirements.txt requirements.txt
COPY config/uwsgi/uwsgi.ini uwsgi.ini
COPY config/entrypoint.sh entrypoint.sh

RUN  mkdir -p /var/www/static/ \
     && mkdir -p /var/www/media/ \
     && mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/ \
     && pip install --no-cache-dir --requirement requirements.txt

COPY . .


EXPOSE 8000

RUN chmod 777 /opt/app/entrypoint.sh

ENTRYPOINT ["/opt/app/entrypoint.sh"]
