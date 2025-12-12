#!/usr/bin/env bash
# Install dependencies
pip install -r requirements.txt

# Collect static files (optional)
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate
