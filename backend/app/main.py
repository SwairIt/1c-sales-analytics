from fastapi import FastAPI
from typing import List
from app.integrations.one_c_client import OneCClient
from app.repositories.sales_repo import SalesRepository
from app.schemas.sales import SaleItem
from app.models.sales import Base
from app.core.db import engine

app = FastAPI(title="FastAPI 1C Analytics Platform")
one_c = OneCClient()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/sync/sales", response_model=List[SaleItem])
async def sync_sales():
    data = await one_c.get_sales()
    await SalesRepository.save_sales(data)
    return data