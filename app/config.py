from functools import lru_cache

from pydantic import AnyUrl, BaseSettings


class Settings(BaseSettings):
    DB_NAME: str = "FECHAS_CDF"
    REDIS_URL: AnyUrl
    REDIS_TLS_URL: AnyUrl
    MONGODB_URL: AnyUrl
    REDIS_OM_URL: AnyUrl


@lru_cache
def get_settings():
    return Settings(**{})
