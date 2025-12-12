#!/bin/bash
set -e  # Exit immediately if any command fails

echo "===== ENTRYPOINT START ====="

# Print environment variables for debugging
echo "DATABASE_URL: $DATABASE_URL"
echo "DJANGO_DEBUG: $DJANGO_DEBUG"
echo "DJANGO_ALLOWED_HOSTS: $DJANGO_ALLOWED_HOSTS"

# Wait a few seconds for PostgreSQL to be ready (optional)
sleep 5

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn herb_project.wsgi:application --bind 0.0.0.0:8000
