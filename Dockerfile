# Базовый образ
FROM python:3.9

# Установка рабочей директории
WORKDIR /app

# Копирование файлов проекта в контейнер
COPY Carculculator /app

# Запуск приложения
ENTRYPOINT ["python", "main.py"]