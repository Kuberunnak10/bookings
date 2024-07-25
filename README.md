# Бронирование Отелей

Этот репозиторий представляет собой API для бронирования отелей.

Стэк технологий: FastAPI, Postgres, SQLAlchemy, Celery, Redis, Docker, а также другими технологиями.

## Руководство по запуску

1. Склонировать проект с github.
2. Создать файл .env-non-dev (рядом) и вставить свои параметры по примеру файла .env-example
3. В папке где находится файл docker-compose.yml прописать следующие команды:
```
docker compose build
docker compose up
```
API находится по URL: http://localhost:9000/v1/docs

Для добавления тестовых данных вам необходимо зарегистрироваться
`/auth/register` и аунтефицироваться `/auth/login`.

Далее используем эндпоинт `/import/{table_name}` и загружаем два файла .csv,
они находятся в проекте `app/importer` (hotels.csv и rooms.csv).

Админ панель находится по URL: http://localhost:9000/admin/login