"""Read and provide runtime configuration."""

from functools import cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from {{ cookiecutter.project_slug }}.models import ServiceEnvironment


class Settings(BaseSettings):
    """Create app settings"""

    model_config = SettingsConfigDict(
        env_prefix="{{ cookiecutter.project_slug }}_", env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    env: ServiceEnvironment = ServiceEnvironment.DEV
    debug: bool = False
    test: bool = False


@cache
def get_config() -> Settings:
    """Get runtime configuration

    :return: Settings instance
    """
    return Settings()
