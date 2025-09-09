"""Provide CLI for application."""

import logging

import click

from {{ cookiecutter.project_slug }} import __version__
from {{ cookiecutter.project_slug }}.config import get_config
from {{ cookiecutter.project_slug }}.logging import initialize_logs


@click.group()
@click.version_option(__version__)
def cli() -> None:
    """Short description of CLI.

    \b
        $ echo "provide a multiline description with a leading \\b"
        $ echo "more commands here"
        $ echo "otherwise, a single indent will pick up proper formatting"

    Conclude by summarizing additional commands
    """  # noqa: D301
    log_level = logging.DEBUG if get_config().debug else logging.INFO
    initialize_logs(log_level)
