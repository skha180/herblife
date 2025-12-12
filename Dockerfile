FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8000

# Run migrations, collectstatic, then start Gunicorn
CMD bash -c "\
python manage.py migrate --noinput && \
python manage.py collectstatic --noinput && \
exec gunicorn herb_project.wsgi:application --bind 0.0.0.0:8000 \
"
