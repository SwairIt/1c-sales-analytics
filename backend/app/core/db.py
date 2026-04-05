from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

# создаем движок для асинхронного подключения
engine = create_async_engine(DATABASE_URL, echo=True)

# создаем фабрику сессий
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# вспомогательная функция для использования в зависимости (Depends)
async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session