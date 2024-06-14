from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings


engine = create_async_engine(settings.database_uri_async, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # type: ignore


Base = declarative_base()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:  # type: ignore
        yield session
