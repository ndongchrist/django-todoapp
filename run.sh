#!/bin/bash

# Wait for the database to be ready
until pg_isready -h db -p 5432 -U postgres; do
  echo "Waiting for PostgreSQL to be ready..."
  sleep 2
done

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the application with Gunicorn
exec gunicorn --bind 0.0.0.0:8000 TodoApp.wsgi:application