#!/bin/bash

# Ждём базу
echo "Waiting for PostgreSQL..."
sleep 5

# Миграции
python manage.py makemigrations
python manage.py migrate

# Запуск сервера
python manage.py runserver 0.0.0.0:8000