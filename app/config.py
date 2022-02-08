from pydantic import AnyUrl, BaseSettings


class Settings(BaseSettings):
    REDIS_URL: AnyUrl
    REDIS_TLS_URL: AnyUrl
