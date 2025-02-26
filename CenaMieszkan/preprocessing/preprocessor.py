import pandas as pd
from CenaMieszkan.utils.logging import get_logger

logger = get_logger(__name__)


def fun_preprocessing(data):
    """
    Funkcja czyści dane: usuwa brakujące wartości i konwertuje typy.
    """
    logger.info("Rozpoczęcie procesu czyszczenia danych.")

    zestaw_danych2 = data.copy()
    logger.debug("Utworzono kopię oryginalnego zestawu danych.")

    # Usunięcie wierszy z brakującymi wartościami
    initial_row_count = len(zestaw_danych2)
    zestaw_danych2.dropna(inplace=True)
    final_row_count = len(zestaw_danych2)
    rows_dropped = initial_row_count - final_row_count
    logger.info(f"Usunięto {rows_dropped} wierszy zawierających brakujące wartości.")

    try:
        zestaw_danych2["squareMeters"] = pd.to_numeric(zestaw_danych2["squareMeters"])
        zestaw_danych2["rooms"] = pd.to_numeric(zestaw_danych2["rooms"]).astype("Int64")
        zestaw_danych2["floor"] = pd.to_numeric(zestaw_danych2["floor"]).astype("Int64")
        zestaw_danych2["buildYear"] = pd.to_numeric(zestaw_danych2["buildYear"]).astype("Int64")
        logger.info("Pomyślnie przekonwertowano typy kolumn.")
    except Exception as e:
        logger.error(f"Błąd podczas konwersji typów kolumn: {e}", exc_info=True)
        return pd.DataFrame()

    logger.info("Proces czyszczenia danych zakończony pomyślnie.")
    return zestaw_danych2



