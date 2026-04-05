from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Fake 1C")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/sales")
def get_sales():
    return [
        {"order_id": i, "amount": i * 100, "date": "2026-04-05"} for i in range(1, 21)
    ]