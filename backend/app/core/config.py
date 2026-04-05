import os

DATABASE_URL = os.environ.get("DATABASE_URL")
FAKE_1C_URL = os.environ.get("FAKE_1C_URL")

# Проверка (можно удалить после отладки)
print("DATABASE_URL =", DATABASE_URL)
print("FAKE_1C_URL =", FAKE_1C_URL)