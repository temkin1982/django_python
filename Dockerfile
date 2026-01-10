# Dockerfile
FROM python:3.11-slim

# Установка зависимостей
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Запуск через entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]