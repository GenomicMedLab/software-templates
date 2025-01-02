"""Read and provide runtime configuration."""

import logging
import os

from .models import Config, ServiceEnvironment


_logger = logging.getLogger(__name__)


_ENV_VARNAME = "{{ cookiecutter.project_slug | upper }}"


def _dev_config() -> Config:
    return Config(env=ServiceEnvironment.DEV, debug=True, test=False)


def _test_config() -> Config:
    return Config(env=ServiceEnvironment.TEST, debug=False, test=True)


def _staging_config() -> Config:
    return Config(env=ServiceEnvironment.STAGING, debug=False, test=False)


def _prod_config() -> Config:
    return Config(env=ServiceEnvironment.PROD, debug=False, test=False)


def _default_config():
    return _dev_config()


_CONFIG_MAP = {
    ServiceEnvironment.DEV: _dev_config,
    ServiceEnvironment.TEST: _test_config,
    ServiceEnvironment.STAGING: _staging_config,
    ServiceEnvironment.PROD: _prod_config,
}


def _set_config() -> Config:
    """Set configs based on environment variable `{{ cookiecutter.project_slug | upper }}_ENV`.

    :return: complete config object with environment-specific parameters
    """
    raw_env_value = os.environ.get(_ENV_VARNAME)
    if not raw_env_value:
        return _default_config()
    try:
        env_value = ServiceEnvironment(raw_env_value.lower())
    except ValueError:
        _logger.error(
            "Unrecognized value for %s: %s. Using default configs",
            _ENV_VARNAME,
            raw_env_value
        )
        return _default_config()
    return _CONFIG_MAP[env_value]()


config = _set_config()
