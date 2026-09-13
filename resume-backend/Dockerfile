FROM python:3.12-slim
RUN apt-get update && apt-get install -y nginx supervisor && rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY resume-backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY resume-backend/app.py .
COPY resume-frontend/index.html /var/www/resume/index.html
COPY resume-frontend/nginx.conf /etc/nginx/sites-available/default
COPY resume-backend/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
