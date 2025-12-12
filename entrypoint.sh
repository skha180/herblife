#!/bin/bash
set -e

echo "===== ENTRYPOINT DEBUG ====="
echo "DATABASE_URL: $DATABASE_URL"
echo "DJANGO_SECRET_KEY: $DJANGO_SECRET_KEY"
echo "DJANGO_DEBUG: $DJANGO_DEBUG"
echo "DJANGO_ALLOWED_HOSTS: $DJANGO_ALLOWED_HOSTS"

# Test database connection safely
echo "Testing database connection..."
python - <<END
import os
import dj_database_url
from django.db import connections
from django.db.utils import OperationalError

db_config = dj_database_url.parse(os.environ.get("DATABASE_URL"))
print("Parsed DB config:", db_config)

try:
    conn = connections['default']
    conn.cursor()
    print("PostgreSQL connection OK")
except OperationalError as e:
    print("PostgreSQL connection FAILED:", e)
END

echo "DEBUG ENTRYPOINT COMPLETE"
tail -f /dev/null
