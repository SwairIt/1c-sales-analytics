#!/bin/bash

# =============================================
# FastAPI + 1C Analytics Platform Setup Script
# macOS / Linux
# =============================================

echo "=== FastAPI + 1C Setup Script ==="

# 1️⃣ Проверка Poetry
if ! command -v poetry &> /dev/null; then
    echo "Poetry не найден. Устанавливаем..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
else
    echo "Poetry уже установлен"
fi

# 2️⃣ Проверка Docker
if ! command -v docker &> /dev/null; then
    echo "Docker не найден. Установите Docker вручную и повторите запуск скрипта."
    exit 1
else
    echo "Docker найден"
fi

if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "Docker Compose не найден. Используйте современный 'docker compose' (в Docker 20+) или установите docker-compose."
    exit 1
else
    echo "Docker Compose найден"
fi

# 3️⃣ Установка зависимостей backend
echo "=== Установка зависимостей backend ==="
cd backend || exit
poetry lock || echo "Lock файл обновлен"
poetry install --no-root
cd ..

# 4️⃣ Установка зависимостей fake_1c
echo "=== Установка зависимостей fake_1c ==="
cd fake_1c || exit
poetry lock || echo "Lock файл обновлен"
poetry install --no-root
cd ..

# 5️⃣ Запуск Docker Compose
echo "=== Поднимаем контейнеры через Docker Compose ==="
cd infra || exit
docker compose up --build