"""Configure useful utilities."""

import logging
from logging.handlers import RotatingFileHandler


def initialize_logs(log_level: int = logging.DEBUG) -> None:
    """Configure logging.

    :param log_level: app log level to set
    """
    if log_level not in {10, 20, 30, 40, 50}:
        msg = f"Unrecognized log level: {log_level}"
        raise ValueError(msg)
    root = logging.getLogger()
    if root.handlers:
        return

    root.setLevel(log_level)
    formatter = logging.Formatter(
        "[%(asctime)s] - %(name)s - %(levelname)s : %(message)s"
    )
    fh = RotatingFileHandler(f"{__package__}.log", maxBytes=5_000_000, backupCount=3)
    fh.setFormatter(formatter)
    root.addHandler(fh)
