from scipy.stats import normaltest
import pandas as pd
from CenaMieszkan.utils import get_logger


class stats_Calculator:
    """ Klasa do obliczeń statystycznych na danych dotyczących mieszkań. """

    logger = get_logger(__name__)

    @staticmethod
    def basic_statistics(cleaned_data):
        """ Oblicza podstawowe statystyki dla danych mieszkań. """
        stats_Calculator.logger.info("Rozpoczynanie obliczeń podstawowych statystyk.")

        try:
            flats_in_city = pd.DataFrame(cleaned_data.groupby('city').size().sort_values(ascending=False)).reset_index()
            flats_in_city.columns = ["Miasto", "Liczba mieszkań"]
            stats_Calculator.logger.info(f"Liczba mieszkań obliczona dla {len(flats_in_city)} miast.")

            mean_price_in_city = pd.DataFrame(cleaned_data.groupby('city')['price'].mean().sort_values(ascending=False)).reset_index()
            mean_price_in_city.columns = ["Miasto", "Średnia cen mieszkań (PLN²)"]

            variance_price_in_city = pd.DataFrame(cleaned_data.groupby('city')['price'].var().sort_values(ascending=False)).reset_index()
            variance_price_in_city.columns = ["Miasto", "Wariancja cen mieszkań (PLN²)"]

            standard_devotion_price_in_city = pd.DataFrame(cleaned_data.groupby('city')['price'].std().sort_values(ascending=False)).reset_index()
            standard_devotion_price_in_city.columns = ["Miasto", "Odchylenie standardowe cen mieszkań (PLN²)"]

            general_stats = cleaned_data.describe()
            stats_Calculator.logger.info("Obliczenia podstawowych statystyk zakończone pomyślnie.")

            return flats_in_city, mean_price_in_city, variance_price_in_city, standard_devotion_price_in_city, general_stats

        except Exception as e:
            stats_Calculator.logger.error(f"Błąd podczas obliczania statystyk: {e}", exc_info=True)
            return None

    @staticmethod
    def quantiles(cleaned_data):
        """ Oblicza kwartyle dla cen mieszkań. """
        stats_Calculator.logger.info("Rozpoczynanie obliczania kwartylów.")

        try:
            Q1 = cleaned_data["price"].quantile(0.25)
            Q3 = cleaned_data["price"].quantile(0.75)
            IQR = Q3 - Q1
            stats_Calculator.logger.info(f"Kwartyle obliczone: Q1={Q1}, Q3={Q3}, IQR={IQR}")

            return Q1, Q3, IQR

        except Exception as e:
            stats_Calculator.logger.error(f"Błąd podczas obliczania kwartylów: {e}", exc_info=True)
            return None

    @staticmethod
    def params_and_normal_test(cleaned_data):
        """ Oblicza statystyki rozkładu oraz przeprowadza test normalności. """
        stats_Calculator.logger.info("Rozpoczynanie testu normalności i obliczania parametrów rozkładu.")

        try:
            stat, p = normaltest(cleaned_data['price'])
            skewness = cleaned_data['price'].skew()
            kurtosis = cleaned_data['price'].kurtosis()

            stats_Calculator.logger.info(f"Statystyka testu: {stat:.4f}, p-wartość: {p:.4f}")
            stats_Calculator.logger.info(f"Skośność (skewness): {skewness}")
            stats_Calculator.logger.info(f"Kurtoza (kurtosis): {kurtosis}")

            if p > 0.05:
                stats_Calculator.logger.info("Dane mają rozkład normalny (p > 0.05).")
            else:
                stats_Calculator.logger.info("Dane NIE mają rozkładu normalnego (p < 0.05).")

            return stat, p, skewness, kurtosis

        except Exception as e:
            stats_Calculator.logger.error(f"Błąd podczas testu normalności: {e}", exc_info=True)
            return None



