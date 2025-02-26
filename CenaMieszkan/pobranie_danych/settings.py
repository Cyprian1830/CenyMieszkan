import os
from pathlib import Path
from dotenv import load_dotenv
from CenaMieszkan.utils.logging import get_logger


class AppConfig:
    """Klasa reprezentująca konfigurację aplikacji."""

    def __init__(self):
        # Inicjalizacja loggera
        self.logger = get_logger(__name__)

        # Załadowanie zmiennych środowiskowych
        self.logger.info("Ładowanie pliku .env...")
        self._load_env()

        # Inicjalizacja zmiennych konfiguracyjnych
        self.logger.info("Inicjalizacja zmiennych konfiguracyjnych...")
        try:
            self.database_url = self._get_env_variable("DATABASE_URL", required=True)
            self.secret_key = self._get_env_variable("SECRET_KEY", "default_secret_key")
            self.debug = self._get_env_variable("DEBUG", "False").lower() == "true"

            self.logger.info("Konfiguracja aplikacji załadowana pomyślnie.")
        except ValueError as e:
            self.logger.error(f"Błąd w konfiguracji aplikacji: {e}")
            raise

    def _load_env(self):
        """Ładuje plik .env z głównego katalogu."""
        base_dir = Path(__file__).resolve().parent
        env_path = base_dir / ".env"

        if env_path.exists():
            load_dotenv(env_path)
            self.logger.info(f"Załadowano zmienne środowiskowe z: {env_path}")
        else:
            self.logger.warning(f"Plik .env nie został znaleziony w: {env_path}")

    def _get_env_variable(self, var_name, default=None, required=False):
        """Zwraca wartość zmiennej środowiskowej lub podaje wartość domyślną."""
        value = os.getenv(var_name, default)
        if required and value is None:
            self.logger.error(f"Zmienna środowiskowa '{var_name}' jest wymagana, ale nie została ustawiona.")
            raise ValueError(f"Environment variable '{var_name}' is required but not set.")

        if value is not None:
            self.logger.info(f"Załadowano zmienną środowiskową: {var_name}")

        return value


# Przykładowe wywołanie
try:
    config = AppConfig()
except ValueError:
    print("Błąd inicjalizacji konfiguracji. Sprawdź logi.")
