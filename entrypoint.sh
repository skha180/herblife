#!/bin/bash
set -e  # Exit immediately if a command fails

echo "===== Starting entrypoint ====="

# Print environment info for debugging
echo "DATABASE_URL = $DATABASE_URL"
echo "DJANGO_DEBUG = $DJANGO_DEBUG"

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn herb_project.wsgi:application --bind 0.0.0.0:8000
