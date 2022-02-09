from fastapi import FastAPI
from loguru import logger

from app.services.redis import get_redis

app = FastAPI()


@app.get("/test")
async def test_redis():

    r = get_redis()

    result = await r.get("test")

    logger.debug(f"result: {result}")
