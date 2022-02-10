from beanie import init_beanie
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from app.config import get_settings
from app.core.default import initial_setup
from app.db.mongodb import get_mongodb
from app.models.productos import ProductoDB
from app.services.redis import get_redis

from .api.api import router as api_router

app = FastAPI()


app.include_router(api_router)


@app.on_event("startup")
async def on_startup():
    s = get_settings()

    r = get_redis()
    FastAPICache.init(RedisBackend(r), prefix="fastapi-cache")

    mongo_client = get_mongodb()
    await init_beanie(mongo_client[s.DB_NAME], document_models=[ProductoDB])

    await initial_setup()
