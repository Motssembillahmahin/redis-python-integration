from collections.abc import Generator
from typing import AsyncGenerator

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session

from src.config import settings
from src.constants import DB_NAMING_CONVENTION


from redis import asyncio as aioredis


DATABASE_URL = str(settings.DATABASE_URL)
REDIS_URL = str(settings.REDIS_URL)

metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)
engine = create_engine(DATABASE_URL, echo=settings.DEBUG, pool_size=10, max_overflow=5)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


edis_pool: aioredis.Redis | None = None


async def init_redis_pool():
    """Initialize Redis connection pool - call at app startup"""
    global redis_pool
    redis_pool = await aioredis.from_url(
        REDIS_URL,
        encoding="utf-8",
        decode_responses=True,
        max_connections=10,
        socket_connect_timeout=5,
        socket_keepalive=True,
    )
    await redis_pool.ping()
    print("Redis pool initialized")


async def close_redis_pool():
    """Close Redis connection pool - call at app shutdown"""
    global redis_pool
    if redis_pool:
        await redis_pool.close()
        print("Redis pool closed")


async def get_redis() -> AsyncGenerator[aioredis.Redis, None]:
    if redis_pool is None:
        raise RuntimeError("Redis not initialized. Call init_redis_pool() at startup")
    yield redis_pool
