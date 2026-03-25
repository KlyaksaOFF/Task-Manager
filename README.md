### Linter status:
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=KlyaksaOFF_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=KlyaksaOFF_python-project-52)

# Python Project "Task Manager"

**Task Manager** — это веб-приложение на Django для управления задачами в команде.  
Пользователи могут создавать задачи, назначать исполнителей, указывать статусы и метки, а также удобно фильтровать список задач.

## Возможности

- Регистрация и аутентификация пользователей
- Создание, редактирование и удаление задач
- Управление статусами задач
- Управление метками (labels)
- Назначение исполнителей
- Фильтрация задач по статусу, исполнителю и меткам

## Технологии

- **Язык:** Python
- **Фреймворк:** Django
- **База данных:** PostgreSQL (production), SQLite (development)
- **Стили:** Bootstrap 5
- **Инструменты:** uv, Ruff, Gunicorn, Docker Compose, Coverage, Makefile

## Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/KlyaksaOFF/python-project-52.git
cd python-project-52
```
### 2. Создайте файл .env в корне проекта 
```bash
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
DEBUG=True
```
### 3. Установка зависимостей 
```bash
make install
```
### 4. Применение миграций
```bash
uv run python manage.py migrate
```
### 5. Запуск проекта
```bash
(Local):
make docker-start

(Production-style Gunicorn):
make render-start
```
### Makefile команды
```bash
make install         # Установка зависимостей через uv
make lint            # Проверка кода через Ruff
make django-tests    # Запуск Django тестов
make test-coverage   # Запуск тестов с coverage-отчётом
make render-start    # Запуск Gunicorn
make docker-start    # Запуск Gunicorn на 0.0.0.0:8000
make docker-build    # Сборка и запуск контейнеров через docker compose
make build           # build script
```
### Тестирование
```bash
make django-tests    # Запуск тестов
make lint            # Линтер
make test-coverage   # Проверка покрытия
```