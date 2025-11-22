from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ["BaseSettingsConfig"]


class BaseSettingsConfig(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        str_strip_whitespace=True,
        use_enum_values=True,
        frozen=True,
        coerce_numbers_to_str=True,
    )
