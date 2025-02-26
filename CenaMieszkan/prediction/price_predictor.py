from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from CenaMieszkan.utils import get_logger, PREDICTION_IMAGES


class PricePredictor:
    def __init__(self, cleaned_data=None, annual_inflation_rate=0.02):
        """Inicjalizacja modelu przewidywania cen mieszkań."""
        self.annual_inflation_rate = annual_inflation_rate
        self.logger = get_logger(__name__)
        self.logger.info("Inicjalizacja klasy PricePredictor.")

        self.output_file = Path(PREDICTION_IMAGES) / "price_predictions.txt"
        self.output_file.parent.mkdir(parents=True, exist_ok=True)  # Tworzenie katalogu, jeśli nie istnieje

        self.model = None
        self.data = None

        if cleaned_data is not None:
            self._prepare_data(cleaned_data)
            self._train_model()
        else:
            self.logger.warning("Brak danych. Model nie został wytrenowany.")

    def _prepare_data(self, cleaned_data):
        """Przygotowanie danych do modelu."""
        self.logger.info("Przygotowanie danych do modelu.")
        try:
            if cleaned_data is None or cleaned_data.empty:
                raise ValueError("Dostarczone dane są puste lub None.")

            self.data = cleaned_data[['city', 'squareMeters', 'rooms', 'floor', 'price']].copy()
            self.data = pd.get_dummies(self.data, columns=['city'], drop_first=True)

            self.logger.info(f"Dane zostały pomyślnie przygotowane. {len(self.data)} rekordów.")

        except Exception as e:
            self.logger.error(f"Błąd podczas przygotowywania danych: {e}")
            raise

    def _train_model(self):
        """Trenuje model RandomForestRegressor na dostępnych danych."""
        self.logger.info("Rozpoczynanie treningu modelu RandomForestRegressor.")
        try:
            if self.data is None or self.data.empty:
                raise ValueError("Brak danych do trenowania modelu.")

            X = self.data.drop(columns=['price'])
            y = self.data['price']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            self.model = RandomForestRegressor()
            self.model.fit(X_train, y_train)

            self.logger.info(f"Model został pomyślnie wytrenowany na {len(X_train)} rekordach.")

        except Exception as e:
            self.logger.error(f"Błąd podczas trenowania modelu: {e}")
            raise

    def predict_price(self, city, min_square_meters, max_square_meters, rooms, floor, target_year):
        """Przewiduje cenę mieszkania dla podanych parametrów."""
        self.logger.info(f"Przewidywanie ceny dla miasta: {city}, {min_square_meters}-{max_square_meters} m², "
                         f"pokoje: {rooms}, piętro: {floor}, rok docelowy: {target_year}.")

        try:
            if self.data is None or self.model is None:
                raise ValueError("Model nie został wytrenowany lub brak danych.")
            city = city.lower()
            city_col = f'city_{city}'
            if city_col not in self.data.columns:
                raise ValueError(f"Brak danych dla miasta: {city}. Upewnij się, że nazwa miasta jest poprawna.")

            predictions = []
            for sqm in range(min_square_meters, max_square_meters + 1):
                input_data = {
                    'squareMeters': [sqm],
                    'rooms': [rooms],
                    'floor': [floor]
                }

                for col in self.data.columns:
                    if col.startswith('city_'):
                        input_data[col] = [1 if col == city_col else 0]

                input_df = pd.DataFrame(input_data).reindex(columns=self.data.columns.drop('price'), fill_value=0)

                predicted_price_2023 = self.model.predict(input_df)[0]
                years_difference = target_year - 2023
                adjusted_price = predicted_price_2023 * ((1 + self.annual_inflation_rate) ** years_difference)
                predictions.append(adjusted_price)

            average_price = np.mean(predictions)
            result = f"Przewidywana średnia cena w {city} w roku {target_year} to: {average_price:.2f} PLN.\n"

            with open(self.output_file, "a", encoding="utf-8") as file:
                file.write(result)

            self.logger.info(f"Wynik zapisany do pliku: {self.output_file}")

            return average_price
        except Exception as e:
            self.logger.error(f"Błąd podczas przewidywania ceny: {e}")
            raise

