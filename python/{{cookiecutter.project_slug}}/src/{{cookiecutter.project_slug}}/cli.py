"""Provide CLI for application."""

import click

from . import __version__
from .logging import initialize_logs


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
    initialize_logs()


# TODO add fastapi serve subcommand
