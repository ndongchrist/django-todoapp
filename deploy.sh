#!/bin/bash

# Variables
APP_DIR="/var/www/django-todoapp"

# Navigate to the application directory
cd $APP_DIR

# Pull the latest changes from the repository
git pull origin main

chmod +x run.sh

# Stop and remove existing containers
docker-compose down

# Build and start containers
docker-compose up -d

echo "✅ Deployment completed successfully!"