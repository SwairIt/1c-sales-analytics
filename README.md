# 1C Sales Analytics Platform

> Платформа аналитики продаж на FastAPI с интеграцией с эмулятором 1С и PostgreSQL. Подходит для тестирования и разработки с использованием Docker.

---

## 🔖 Содержание

- [Функции](#feautures)
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Эндпоинты API](#эндпоинты-api)
- [Доступ к сервисам](#доступ-к-сервисам)
- [Доступ к базе данных](#доступ-к-базе-данных)
- [Тестирование и разработка](#тестирование-и-разработка)

---

## Функции

Этот проект позволяет:

- Backend на FastAPI для аналитики продаж
- Эмулятор сервера 1С (fake_1c) для тестирования
- PostgreSQL для хранения данных
- Поддержка Docker и Docker Compose
- Асинхронный HTTP-клиент для получения данных о продажах
- Документация API через Swagger UI (/docs)

---

## Структура проекта

```text
fastapi-1c-analytics-platform/
├─ backend/           # FastAPI backend
├─ fake_1c/           # Имитация 1С
├─ infra/             # Docker Compose
├─ setup.sh           # Bash скрипт для macOS/Linux
├─ setup.ps1          # PowerShell скрипт для Windows
└─ README.md
```

---

## Технологии
- Python 3.11
- FastAPI
- SQLAlchemy + PostgreSQL
- Docker & Docker Compose
- httpx (асинхронный HTTP-клиент)
- Poetry (управление зависимостями)

---

## Установка и запуск
macOS / Linux
Клонируем проект:
```Bash
git clone https://github.com/<ваш_репозиторий>/fastapi-1c-analytics-platform.git
cd fastapi-1c-analytics-platform
```
Делаем скрипт исполняемым:
```Bash
chmod +x setup.sh
```
Запускаем его:
```Bash
./setup.sh
```
Скрипт проверит наличие Poetry, установит зависимости backend и fake_1c, а затем поднимет все контейнеры Docker.
Endpoint /sync/sales → получить 20 фейковых заказов → сохранение в PostgreSQL.

---

## Windows (PowerShell)
Открываем PowerShell и клонируем проект:
```PowerShell
git clone https://github.com/<ваш_репозиторий>/fastapi-1c-analytics-platform.git
cd fastapi-1c-analytics-platform
```
Запускаем скрипт:
```PowerShell
.\setup.ps1
```
Скрипт проверит Poetry, установит зависимости, поднимет контейнеры через Docker Compose.

---

## Эндпоинты API
GET /health — проверка статуса сервиса
GET /sync/sales — синхронизация данных из Fake 1C, возвращает список заказов:
```JSON
[
  {
    "order_id": 1,
    "amount": 100,
    "date": "2026-04-05"
  },
  ...
]
```

---

## Доступ к сервисам
- FastAPI API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- Эмулятор 1С (fake_1c): http://localhost:9000/sales
- PgAdmin (если добавлен) по умолчанию: http://localhost:8080

---

## Доступ к базе данных
- PostgreSQL доступен на порту 5432
- Подключение через любой клиент с использованием данных из .env
- Таблицы создаются автоматически SQLAlchemy
- Чтобы полностью очистить базу, выполните:
```
docker-compose down -v
```
Это удалит все данные и тома

---

## Тестирование и разработка
- Изменяйте fake_1c/server.py, чтобы менять тестовые данные
- API и сервер fake_1c работают асинхронно
- Для тестирования используйте Swagger UI
