import logging


def get_logger(
    name: str, log_file: str = "app.log", level: int = logging.DEBUG
) -> logging.Logger:
    """
    Tworzy logger z logowaniem strumieniowym i do pliku.

    :param name: Nazwa loggera.
    :param log_file: Ścieżka do pliku logów.
    :param level: Poziom logowania (np. logging.DEBUG, logging.INFO).
    :return: Skonfigurowany logger.
    """
    # Utwórz logger z podaną nazwą
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Upewnij się, że logger nie powiela komunikatów
    logger.propagate = False

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Handler strumieniowy (konsola)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)  # Set level for stream
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # File handler
    file_handler = logging.FileHandler(log_file, mode="a")
    file_handler.setLevel(logging.ERROR)  # Set level for file
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
