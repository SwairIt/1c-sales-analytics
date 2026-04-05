import httpx
from app.core.config import FAKE_1C_URL

class OneCClient:

    async def get_sales(self):
        async with httpx.AsyncClient() as client:
            url = f"{FAKE_1C_URL}/sales"  
            resp = await client.get(url)
            resp.raise_for_status()
            return resp.json()