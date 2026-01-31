from pathlib import Path

from pydantic import HttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    base_url: HttpUrl = HttpUrl("https://futuramaapi.com")

    @property
    def project_root(self) -> Path:
        return Path(__file__).parent.parent.parent.parent.resolve()


settings: Settings = Settings()
