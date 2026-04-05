# FastAPI + 1C Analytics Platform

> Полноценная интеграционная платформа для работы с данными из 1С и аналитики через FastAPI и PostgreSQL.

---

## 🔖 Содержание

- [О проекте](#%D0%BE-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B5)
- [Структура проекта](#%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
- [Требования](#%D1%82%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
- [Установка и запуск](#%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-%D0%B8-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA)
  - [macOS / Linux](#macos--linux)
  - [Windows (PowerShell)](#windows-powershell)
- [Endpoints API](#endpoints-api)

---

## 🔹 О проекте

Этот проект позволяет:

- Интегрировать данные из 1С в Python-платформу
- Сохранять данные в PostgreSQL для аналитики
- Предоставлять REST API для фронтенда (React/Vue) или BI-дашбордов
- Разрабатывать и тестировать интеграцию без реальной 1С (используется Fake 1C)

---

## 🔹 Структура проекта

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

## 🔹 Требования
Python 3.11+
Poetry
Docker + Docker Compose
Git (для клонирования проекта)

---

## 🔹 Установка и запуск
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

## 🔹 Endpoints API
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