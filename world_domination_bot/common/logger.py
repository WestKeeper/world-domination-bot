""""""
import logging
from logging import Logger


def setup_logging() -> Logger:
    """"""
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger
