release: python manage.py migrate --noinput
web: daphne django_chatroom.asgi:application --port 6379 --bind 0.0.0.0
worker: REMAP_SIGTERM=SIGQUIT celery worker --app django_chatroom.celery.app --loglevel info