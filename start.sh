#!/bin/bash

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start gunicorn
exec gunicorn cronos_project.wsgi:application --bind 0.0.0.0:$PORT --timeout 120 --workers 1 --log-file - 