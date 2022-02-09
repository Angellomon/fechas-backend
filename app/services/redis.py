from functools import lru_cache

import aioredis
from app.config import get_settings

s = get_settings()


@lru_cache
def get_redis() -> aioredis.Redis:
    return aioredis.from_url(s.REDIS_URL)
