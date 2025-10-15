from redis.asyncio import Redis


async def set_product(redis: Redis, name: str):
    await redis.set("products:1", f"{name}")
    value = await redis.get("products:1")
    return {"product": value}
