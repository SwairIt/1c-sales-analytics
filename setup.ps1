# =============================================
# FastAPI + 1C Analytics Platform Setup Script
# Windows PowerShell
# =============================================

Write-Host "=== FastAPI + 1C Setup Script ==="

# 1️⃣ Проверка Poetry
if (-not (Get-Command poetry -ErrorAction SilentlyContinue)) {
    Write-Host "Poetry не найден. Устанавливаем..."
    Invoke-Expression "& { $(Invoke-RestMethod https://install.python-poetry.org) }"
} else {
    Write-Host "Poetry уже установлен"
}

# 2️⃣ Проверка Docker
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "Docker не найден. Установите Docker Desktop и повторите запуск."
    exit 1
}

# 3️⃣ Установка зависимостей backend
Write-Host "=== Установка зависимостей backend ==="
Set-Location .\backend
poetry lock
poetry install --no-root
Set-Location ..

# 4️⃣ Установка зависимостей fake_1c
Write-Host "=== Установка зависимостей fake_1c ==="
Set-Location .\fake_1c
poetry lock
poetry install --no-root
Set-Location ..

# 5️⃣ Запуск Docker Compose
Write-Host "=== Поднимаем контейнеры через Docker Compose ==="
Set-Location .\infra
docker compose up --build