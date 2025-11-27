from pydantic import PostgresDsn

from settings._base import BaseSettingsConfig

__all__ = ["DatabaseSettings"]


class DatabaseSettings(BaseSettingsConfig, env_prefix='DATABASE_'):
    POSTGRES_DSN: PostgresDsn
