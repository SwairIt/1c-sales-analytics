FROM python:3.11-slim
RUN pip install --no-cache-dir poetry
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root
COPY . /app
EXPOSE 9000
CMD ["poetry", "run", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]