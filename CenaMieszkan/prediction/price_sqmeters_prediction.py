import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from CenaMieszkan.utils import PREDICTION_IMAGES, get_logger


class FuturePricePredictor:
    def __init__(self, data, annual_inflation_rate=0.02, output_dir=PREDICTION_IMAGES):
        self.data = data
        self.annual_inflation_rate = annual_inflation_rate
        self.output_dir = output_dir
        self.model = None
        self.logger = get_logger(__name__)
        self._prepare_data()
        self._ensure_output_dir()

    def _prepare_data(self):
        """Przygotowuje dane do treningu modelu."""
        self.data = pd.get_dummies(self.data, columns=['city'], drop_first=True)
        self.logger.info("Dane zostały przygotowane do treningu.")

    def _ensure_output_dir(self):
        """Zapewnia istnienie katalogu wyjściowego do zapisu wykresów."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)
            self.logger.info(f"Utworzono katalog dla obrazów: {self.output_dir}")
        else:
            self.logger.info(f"Katalog dla obrazów już istnieje: {self.output_dir}")

    def train_model(self):
        """Trenuje model RandomForestRegressor na przygotowanych danych."""
        X = self.data.drop(columns='price')
        y = self.data['price']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = RandomForestRegressor()
        self.model.fit(X_train, y_train)
        self.logger.info("Model został wytrenowany.")

    def predict_average_price(self, city, min_sq_meters, max_sq_meters, rooms, floor):
        """
        Przewiduje średnią cenę mieszkania w zadanym mieście i zakresie powierzchni
        na podstawie wytrenowanego modelu, uwzględniając inflację od 2024 roku.
        """
        if self.model is None:
            self.logger.error("Model nie został wytrenowany. Użyj metody 'train_model' przed przewidywaniem.")
            return None

        predicted_prices_2024 = []

        for sq_meters in range(min_sq_meters, max_sq_meters + 1):
            input_data = {
                'squareMeters': [sq_meters],
                'rooms': [rooms],
                'floor': [floor]
            }

            for col in self.data.columns:
                if col.startswith('city_'):
                    input_data[col] = [1 if col == f'city_{city}' else 0]

            input_df = pd.DataFrame(input_data)
            input_df = input_df.reindex(columns=self.data.drop(columns='price').columns, fill_value=0)

            predicted_price_2024 = self.model.predict(input_df)[0]
            predicted_prices_2024.append(predicted_price_2024)

        avg_price_2024 = np.mean(predicted_prices_2024)
        self.logger.info(f"Średnia przewidywana cena w 2024 roku: {avg_price_2024:.2f} PLN")

        years = list(range(2024, 2051))
        avg_prices = [avg_price_2024 * ((1 + self.annual_inflation_rate) ** (year - 2024)) for year in years]

        return years, avg_prices

    def plot_price_forecast(self, city, min_sq_meters, max_sq_meters, rooms, floor):
        """
        Generuje i zapisuje wykres prognozy średnich cen mieszkań w zadanym mieście
        i zakresie powierzchni od 2024 do 2050 roku.
        """
        result = self.predict_average_price(city, min_sq_meters, max_sq_meters, rooms, floor)
        if result is None:
            return

        years, avg_prices = result

        plt.figure(figsize=(12, 6))
        plt.scatter(years, avg_prices, color='blue', label='Prognozowana średnia cena')
        plt.plot(years, avg_prices, color='red', linestyle='--')
        plt.title(f'Prognoza średnich cen mieszkań w mieście {city.capitalize()} (pow. {min_sq_meters}-{max_sq_meters} m²)')
        plt.xlabel('Rok')
        plt.ylabel('Cena (PLN)')
        plt.grid(True)
        plt.legend()

        file_name = f"{city}_{min_sq_meters}_{max_sq_meters}_price_forecast.jpg"
        file_path = os.path.join(self.output_dir, file_name)
        plt.savefig(file_path, format='jpg')
        plt.close()
        self.logger.info(f"Wykres został zapisany pod ścieżką: {file_path}")



