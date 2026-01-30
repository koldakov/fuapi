from pydantic import HttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    base_url: HttpUrl = HttpUrl("https://futuramaapi.com")


settings: Settings = Settings()
