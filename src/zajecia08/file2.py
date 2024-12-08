from src.zajecia08.utils.logging import get_logger

_logger = get_logger("ModuleTwo", "./file2.py")


def module_two_function():
    _logger.debug("Rozpoczynam działanie funkcji w module two.")
    _logger.info("To jest komunikat informacyjny z module_two.")
    try:
        _ = 1 / 0
    except ZeroDivisionError as e:
        _logger.error(f"Błąd dzielenia przez zero: {e}")
    _logger.warning("To jest ostrzeżenie z module_two.")
    _logger.critical("To jest komunikat krytyczny z module_two.")


module_two_function()
# 2024-12-08 10:59:26,671 - ModuleTwo - ERROR - B��d dzielenia przez zero: division by zero
# 2024-12-08 10:59:26,672 - ModuleTwo - CRITICAL - To jest komunikat krytyczny z module_two.
