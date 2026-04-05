from app.models.sales import Sale
from app.core.db import AsyncSessionLocal

class SalesRepository:

    @staticmethod
    async def save_sales(data):
        async with AsyncSessionLocal() as session:
            for item in data:
                sale = Sale(order_id=item['order_id'], amount=item['amount'], date=item['date'])
                session.add(sale)
            await session.commit()