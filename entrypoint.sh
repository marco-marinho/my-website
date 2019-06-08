#!/bin/sh
# Migrate the database first

python manage.py flush --no-input
python manage.py collectstatic --noinput --clear
python manage.py makemigrations --noinput
python manage.py migrate --noinput
#exec gunicorn site_pessal.wsgi:application --bind 0.0.0.0:8000 --workers 3

exec "$@"