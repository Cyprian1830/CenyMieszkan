from __future__ import annotations
import logging


def get_logger(name: str, log_level: int | str = logging.INFO) -> logging.Logger:
    """
        Logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    if not logger.handlers:
        formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger
