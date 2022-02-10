from functools import lru_cache

import motor
from app.config import get_settings

s = get_settings()


@lru_cache
def get_mongodb() -> motor.motor_asyncio.AsyncIOMotorClient:
    return motor.motor_asyncio.AsyncIOMotorClient(s.MONGODB_URL)
