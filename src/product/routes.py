from typing import Annotated
from fastapi import APIRouter, Depends
from src.database import get_redis
from redis.asyncio import Redis
from . import services


router = APIRouter()


@router.get("")
async def get_root(redis: Annotated[Redis, Depends(get_redis)]):
    await redis.set("user:1", "John")
    value = await redis.get("user:1")
    return {"value": value}


@router.post("")
async def set_products(redis: Annotated[Redis, Depends(get_redis)], name: str):
    response = await services.set_product(redis, name)
    return response
