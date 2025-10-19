# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
# Core
from app.core.settings import settings
# AsyncPG
import asyncpg.exceptions


engine = create_async_engine(settings.database_url)
async_session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

async def get_db() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        except asyncpg.exceptions.ConnectionDoesNotExistError:
            raise
        finally:
            await session.close()
