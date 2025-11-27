from pathlib import Path
from typing import Annotated

from pydantic import Field

from settings._base import BaseSettingsConfig
# from settings.database import DatabaseSettings
from settings.server import ServerSettings

__all__ = ["Settings"]


class Settings(BaseSettingsConfig):
    BASE_DIR: Path = Path(__file__).parent.parent

    SERVER: Annotated[ServerSettings, Field(default_factory=ServerSettings)]
    # DATABASE: Annotated[DatabaseSettings, Field(default_factory=DatabaseSettings)]


settings = Settings()
