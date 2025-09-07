#!/bin/bash

# Variables
APP_DIR="/var/www/django-todoapp"
VENV_DIR="$APP_DIR/venv"
REQUIREMENTS_FILE="$APP_DIR/requirements.txt"

# Navigate to the application directory
cd $APP_DIR

# Pull the latest changes from the repository
git pull origin main

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Install dependencies
pip install -r $REQUIREMENTS_FILE

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart the application (e.g., using systemctl)
python manage.py runserver 0.0.0:8000
