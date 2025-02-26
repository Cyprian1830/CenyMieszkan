import os
import matplotlib.pyplot as plt
import seaborn as sns
from CenaMieszkan.utils import PREDICTION_IMAGES, get_logger


class PriceAnalyzer:
    def __init__(self, output_dir: str = PREDICTION_IMAGES):
        self.output_dir = output_dir
        self.logger = get_logger(__name__)
        self._ensure_output_dir()

    def _ensure_output_dir(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)
            self.logger.info(f"Utworzono katalog dla obrazów: {self.output_dir}")
        else:
            self.logger.info(f"Katalog dla obrazów już istnieje: {self.output_dir}")

    def square_meters_price(self, city: str, min_sq_meters: int, max_sq_meters: int, cleaned_data=None):
        self.logger.info(f"Rozpoczęcie analizy dla miasta: {city}, zakres powierzchni: {min_sq_meters}-{max_sq_meters} m²")

        city = city.lower()
        filtered_data = cleaned_data[
            (cleaned_data['city'].str.lower() == city) &
            (cleaned_data['squareMeters'] >= min_sq_meters) &
            (cleaned_data['squareMeters'] <= max_sq_meters)
        ]

        if filtered_data.empty:
            self.logger.warning(f"Brak danych dla miasta {city.capitalize()} w zakresie {min_sq_meters}-{max_sq_meters} m².")
            return

        self.logger.info(f"Znaleziono {len(filtered_data)} rekordów spełniających kryteria.")

        plt.figure(figsize=(10, 6))
        sns.lmplot(
            data=filtered_data,
            x='squareMeters',
            y='price',
            height=6,
            aspect=1.5,
            ci=None,
            line_kws={'color': 'red'}
        )
        plt.title(f'Zależność ceny od powierzchni mieszkań w mieście {city.capitalize()}')
        plt.xlabel('Powierzchnia (m²)')
        plt.ylabel('Cena (PLN)')
        plt.grid(True)

        file_name = f"{city}_{min_sq_meters}_{max_sq_meters}_price_analysis.jpg"
        file_path = os.path.join(self.output_dir, file_name)
        plt.savefig(file_path, format='jpg')
        plt.close()
        self.logger.info(f"Wykres został zapisany pod ścieżką: {file_path}")


