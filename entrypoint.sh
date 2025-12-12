#!/bin/bash
set -e

echo "===== ENTRYPOINT START ====="
echo "DATABASE_URL: $DATABASE_URL"
echo "DJANGO_DEBUG: $DJANGO_DEBUG"
echo "DJANGO_ALLOWED_HOSTS: $DJANGO_ALLOWED_HOSTS"
echo "BASE_DIR: $BASE_DIR"

# Test Python environment
python --version
pip list

# Exit so container doesn’t crash
echo "Entrypoint debug complete"
tail -f /dev/null
