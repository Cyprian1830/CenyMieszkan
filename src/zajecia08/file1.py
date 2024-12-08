from src.zajecia08.utils.logging import get_logger

_logger = get_logger("ModuleOne", "./file1.py")


def module_one_function():
    _logger.debug("Rozpoczynam działanie funkcji w module one.")
    _logger.info("To jest komunikat informacyjny z module_one.")
    _logger.warning("To jest ostrzeżenie z module_one.")
    try:
        raise ValueError("Przykładowy błąd w module one.")
    except ValueError as e:
        _logger.error(f"Złapano wyjątek: {e}")
    _logger.critical("To jest komunikat krytyczny z module_one.")


module_one_function()
# 2024-12-08 10:57:37,820 - ModuleOne - ERROR - Z�apano wyj�tek: Przyk�adowy b��d w module one.
# 2024-12-08 10:57:37,826 - ModuleOne - CRITICAL - To jest komunikat krytyczny z module_one.
