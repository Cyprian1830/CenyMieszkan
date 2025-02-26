import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from CenaMieszkan.pobranie_danych.settings import AppConfig
from CenaMieszkan.utils.logging import get_logger


class DatabaseManager:
    """Klasa zarządzająca operacjami na bazie danych."""

    def __init__(self):
        # Inicjalizacja loggera
        self.logger = get_logger(__name__)

        # Załadowanie konfiguracji
        self.logger.info("Ładowanie konfiguracji bazy danych...")
        config = AppConfig()
        self.engine = create_engine(config.database_url, echo=config.debug)
        self.Session = sessionmaker(bind=self.engine)
        self.logger.info("Połączenie z bazą danych zostało skonfigurowane.")

    def select(self):
        """ Pobiera dane z bazy danych i zwraca je jako DataFrame """
        self.logger.info("Rozpoczynanie operacji SELECT na bazie danych...")
        try:
            with self.Session() as session:
                raw_sql = text("""
                    SELECT city, squareMeters, rooms, floor, buildYear, price 
                    FROM dbo.ceny_mieszkań
                """)
                result = session.execute(raw_sql)
                rows = result.fetchall()

                if not rows:
                    self.logger.warning("Zapytanie nie zwróciło żadnych wyników.")
                else:
                    self.logger.info(f"Pobrano {len(rows)} rekordów z bazy danych.")

                dane = pd.DataFrame(rows, columns=["city", "squareMeters", "rooms", "floor", "buildYear", "price"])
                return dane

        except Exception as e:
            self.logger.error(f"Błąd podczas wykonywania zapytania SELECT: {e}", exc_info=True)
            return pd.DataFrame()  # Zwraca pusty DataFrame w razie błędu


db_manager2 = DatabaseManager()
zestaw_danych = db_manager2.select()

if not zestaw_danych.empty:
    db_manager2.logger.info(f"Pobrane dane:\n{zestaw_danych.head()}")
else:
    db_manager2.logger.warning("Brak danych do wyświetlenia.")

print(zestaw_danych)
