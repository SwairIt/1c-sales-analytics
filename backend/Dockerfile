FROM python:3.11-slim

WORKDIR /app

# Установим системные зависимости для psycopg2-binary
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Poetry
RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root


COPY . /app

EXPOSE 8000

# Запуск через Poetry, чтобы uvicorn был доступен
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]