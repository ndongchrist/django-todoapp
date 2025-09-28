#!/bin/bash

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the application with Gunicorn
exec gunicorn --bind 0.0.0.0:8000 TodoApp.wsgi:application