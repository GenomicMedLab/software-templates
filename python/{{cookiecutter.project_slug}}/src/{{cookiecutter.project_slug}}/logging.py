"""Configure application logging."""

import logging


def initialize_logs(log_level: int = logging.DEBUG) -> None:
    """Configure logging.

    :param log_level: app log level to set
    """
    log_filename = f"{__package__}.log"
    logging.basicConfig(
        filename=log_filename,
        format="[%(asctime)s] - %(name)s - %(levelname)s : %(message)s",
    )
    logger = logging.getLogger(__package__)
    logger.setLevel(log_level)
