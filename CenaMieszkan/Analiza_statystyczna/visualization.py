import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.ticker as ticker
from CenaMieszkan.utils.consts import IMAGES
from CenaMieszkan.utils.logging import get_logger


class Visualizer:

    def __init__(self, output_dir: str = None):
        """Inicjalizacja klasy wizualizera."""
        self.output_dir = output_dir if isinstance(output_dir, str) else IMAGES
        self.logger = get_logger(__name__)

        # Tworzymy katalog na obrazy, jeśli nie istnieje
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)
            self.logger.info(f"Utworzono katalog dla obrazów: {self.output_dir}")
        else:
            self.logger.info(f"Katalog dla obrazów już istnieje: {self.output_dir}")

    def _validate_data(self, cleaned_data):
        """ Sprawdza, czy przekazane dane są prawidłowym DataFrame. """
        if cleaned_data is None or not isinstance(cleaned_data, pd.DataFrame) or cleaned_data.empty:
            self.logger.error("❌ Błąd: przekazane dane są puste lub nie są DataFrame.")
            return False
        return True

    def scatterplot_plot(self, cleaned_data, output_dir: str = None):
        """ Tworzy wykres zależności ceny od metrażu mieszkań i zapisuje go jako obraz. """
        if not self._validate_data(cleaned_data):
            return

        output_dir = output_dir if isinstance(output_dir, str) else self.output_dir

        self.logger.info("Tworzenie wykresu zależności ceny od metrażu mieszkań.")
        plt.figure(figsize=(10, 5))
        sns.scatterplot(x=cleaned_data["squareMeters"], y=cleaned_data["price"], alpha=0.6)

        plt.title("Zależność ceny od metrażu", fontsize=12)
        plt.xlabel("Powierzchnia mieszkania (m²)", fontsize=10)
        plt.ylabel("Cena mieszkania (PLN)", fontsize=10)
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x / 1e6:.1f} × 10⁶'))

        file_path = os.path.join(output_dir, "scatter_plot_cen_mieszkań.jpg")
        plt.savefig(file_path, format='jpg')
        plt.close()
        self.logger.info(f"Wykres zapisano jako: {file_path}")

    def boxplots(self, cleaned_data, output_dir: str = None):
        """ Tworzy wykresy pudełkowe dla cen mieszkań w różnych miastach. """
        if not self._validate_data(cleaned_data):
            return

        output_dir = output_dir if isinstance(output_dir, str) else self.output_dir

        self.logger.info("Tworzenie wykresów pudełkowych.")
        fig, axes = plt.subplots(2, 1, figsize=(15, 15))
        fig.suptitle("Wykresy: ")

        sns.boxplot(data=cleaned_data, x="city", y="price", hue="city", palette="viridis", ax=axes[0], showmeans=True)
        sns.boxplot(data=cleaned_data, x="city", y="squareMeters", hue="city", palette="viridis", ax=axes[1], showmeans=True)

        file_path = os.path.join(output_dir, "boxplot_cen_mieszkań.jpg")
        plt.savefig(file_path, format='jpg')
        plt.close()
        self.logger.info(f"Wykres zapisano jako: {file_path}")

    def outer_score_values(self, cleaned_data, output_dir: str = None):
        """ Tworzy wykres wartości odstających dla cen mieszkań. """
        if not self._validate_data(cleaned_data):
            return

        output_dir = output_dir if isinstance(output_dir, str) else self.output_dir

        self.logger.info("Tworzenie wykresu wartości odstających.")
        plt.figure(figsize=(10, 5))
        sns.boxplot(x=cleaned_data["price"])
        plt.title("Wartości odstające cen mieszkań")
        plt.xlabel("Cena (PLN)")
        plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x / 1e6:.1f} × 10⁶'))

        file_path = os.path.join(output_dir, "wartosci_odstajace_cen_mieszkań.jpg")
        plt.savefig(file_path, format='jpg')
        plt.close()
        self.logger.info(f"Wykres zapisano jako: {file_path}")

    def corr_map(self, cleaned_data, output_dir: str = None):
        """ Tworzy macierz korelacji i zapisuje ją jako obraz. """
        if not self._validate_data(cleaned_data):
            return

        output_dir = output_dir if isinstance(output_dir, str) else self.output_dir

        self.logger.info("Tworzenie macierzy korelacji.")
        selected_columns = ["squareMeters", "rooms", "floor", "buildYear", "price"]
        corr_matrix = cleaned_data[selected_columns].corr()

        plt.figure(figsize=(8, 5))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Macierz korelacji wybranych zmiennych")

        file_path = os.path.join(output_dir, "mapa_korelacji_cen_mieszkań.jpg")
        plt.savefig(file_path, format='jpg')
        plt.close()
        self.logger.info(f"Wykres zapisano jako: {file_path}")

    def distribution_function(self, cleaned_data, output_dir: str = None):
        """ Tworzy histogram rozkładu cen mieszkań. """
        if not self._validate_data(cleaned_data):
            return

        output_dir = output_dir if isinstance(output_dir, str) else self.output_dir

        self.logger.info("Tworzenie histogramu rozkładu cen mieszkań.")
        plt.figure(figsize=(10, 5))
        sns.histplot(cleaned_data["price"], bins=50, kde=True)

        plt.title("Rozkład cen mieszkań", fontsize=12)
        plt.xlabel("Cena mieszkania (PLN)", fontsize=10)
        plt.ylabel("Liczba mieszkań", fontsize=10)
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x / 1e6:.1f} × 10⁶'))

        file_path = os.path.join(output_dir, "rozkład_gęstości_cen_mieszkań.jpg")
        plt.savefig(file_path, format='jpg')
        plt.close()
        self.logger.info(f"Wykres zapisano jako: {file_path}")
