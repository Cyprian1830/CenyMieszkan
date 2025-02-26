from __future__ import annotations
import click
from CenaMieszkan.pobranie_danych.db_manager import DatabaseManager
from CenaMieszkan.prediction.city_sqmeters_price import PriceAnalyzer
from CenaMieszkan.prediction.price_predictor import PricePredictor
from CenaMieszkan.prediction.price_sqmeters_prediction import FuturePricePredictor
from CenaMieszkan.preprocessing.preprocessor import fun_preprocessing
from CenaMieszkan.utils.logging import get_logger
from CenaMieszkan.Analiza_statystyczna.statistics_analysis import stats_Calculator
from CenaMieszkan.Analiza_statystyczna.visualization import Visualizer

logger = get_logger("APPLICATION")


@click.group()
def cli() -> None:
    """Interfejs CLI do analizy danych mieszkań."""


@cli.command()
def general_process():
    """ Pobiera dane z bazy danych i przetwarza je. """
    logger.info("Pobieranie danych z bazy...")

    try:
        db_manager = DatabaseManager()
        data = db_manager.select()

        if data.empty:
            click.echo("Brak danych do przetworzenia.")
            return None

        cleaned_data = fun_preprocessing(data)
        click.echo("Dane zostały pomyślnie przetworzone.")
        return cleaned_data

    except Exception as e:
        logger.error(f"Błąd podczas pobierania i przetwarzania danych: {e}", exc_info=True)
        click.echo(f"Błąd: {e}")
        return None


@cli.command()
@click.pass_context
def analysis_and_visualization(ctx):
    """ Przeprowadza analizę statystyczną i tworzy wizualizacje na podstawie przetworzonych danych. """
    logger.info("Rozpoczynanie analizy i wizualizacji...")

    cleaned_data = ctx.invoke(general_process)

    if cleaned_data is None:
        click.echo("Nie można przeprowadzić analizy, brak danych.")
        return

    try:
        calculator = stats_Calculator()
        click.echo("Obliczanie statystyk...")
        calculator.basic_statistics(cleaned_data)
        calculator.quantiles(cleaned_data)
        calculator.params_and_normal_test(cleaned_data)
        click.echo("Statystyki zostały obliczone.")

        visualizer = Visualizer()
        click.echo("Tworzenie wizualizacji...")
        visualizer.scatterplot_plot(cleaned_data)
        visualizer.boxplots(cleaned_data)
        visualizer.outer_score_values(cleaned_data)
        visualizer.corr_map(cleaned_data)
        visualizer.distribution_function(cleaned_data)
        click.echo("Wizualizacje zostały wygenerowane.")

    except Exception as e:
        logger.error(f"Błąd podczas analizy i wizualizacji: {e}", exc_info=True)
        click.echo(f"Błąd: {e}")


@cli.command()
@click.argument("city", type=str)
@click.argument("min_sq_meters", type=int)
@click.argument("max_sq_meters", type=int)
@click.pass_context
def price_analysis(ctx, city, min_sq_meters, max_sq_meters):
    """
    Analizuje zależność ceny od powierzchni mieszkań dla podanego miasta i zakresu m².
    """
    logger.info(f"Analiza cen mieszkań dla miasta: {city}, powierzchnia: {min_sq_meters}-{max_sq_meters} m²")

    cleaned_data = ctx.invoke(general_process)

    if cleaned_data is None:
        click.echo("Nie można przeprowadzić analizy, brak danych.")
        return

    try:
        analyzer = PriceAnalyzer()
        analyzer.square_meters_price(city, min_sq_meters, max_sq_meters, cleaned_data)
        click.echo(f"Wykres analizy cen dla miasta {city.capitalize()} został wygenerowany.")

    except Exception as e:
        logger.error(f"Błąd podczas analizy cen: {e}", exc_info=True)
        click.echo(f"Błąd: {e}")


@cli.command()
@click.argument("city", type=str)
@click.argument("min_sq_meters", type=int)
@click.argument("max_sq_meters", type=int)
@click.argument("rooms", type=int)
@click.argument("floor", type=int)
@click.argument("target_year", type=int)
@click.pass_context
def predict_price(ctx, city, min_sq_meters, max_sq_meters, rooms, floor, target_year):
    """
    Przewiduje cenę mieszkania na podstawie danych historycznych i inflacji.
    """
    logger.info(
        f"Przewidywanie ceny dla {city}, {min_sq_meters}-{max_sq_meters} m², {rooms} pokoi, piętro {floor}, rok {target_year}")

    cleaned_data = ctx.invoke(general_process)

    if cleaned_data is None:
        click.echo("Nie można przeprowadzić przewidywania, brak danych.")
        return

    try:
        predictor = PricePredictor(cleaned_data)
        predicted_price = predictor.predict_price(city, min_sq_meters, max_sq_meters, rooms, floor, target_year)
        click.echo(f"Przewidywana cena dla {city} w roku {target_year}: {predicted_price:.2f} PLN.")

    except Exception as e:
        logger.error(f"Błąd podczas przewidywania ceny: {e}", exc_info=True)
        click.echo(f"Błąd: {e}")


@cli.command()
@click.argument("city", type=str)
@click.argument("min_sq_meters", type=int)
@click.argument("max_sq_meters", type=int)
@click.argument("rooms", type=int)
@click.argument("floor", type=int)
@click.pass_context
def run_forecast(ctx, city, min_sq_meters, max_sq_meters, rooms, floor):
    """
    Wykonuje pełny proces prognozowania cen mieszkań.
    """
    click.echo("Pobieranie danych...")
    db_manager = DatabaseManager()
    data = db_manager.select()

    if data.empty:
        click.echo("Brak danych. Nie można przeprowadzić prognozy.")
        return

    click.echo("Przetwarzanie danych...")
    cleaned_data = fun_preprocessing(data)

    click.echo("Trenowanie modelu...")
    predictor = FuturePricePredictor(cleaned_data)
    predictor.train_model()

    click.echo(f"Przewidywanie cen mieszkań dla {city.capitalize()}...")
    years, avg_prices = predictor.predict_average_price(city, min_sq_meters, max_sq_meters, rooms, floor)

    click.echo(f"Prognoza cen mieszkań w {city.capitalize()} (pow. {min_sq_meters}-{max_sq_meters} m²):")
    for year, price in zip(years, avg_prices):
        click.echo(f"{year}: {price:.2f} PLN")

    click.echo(f"Generowanie wykresu prognozy cen dla {city.capitalize()}...")
    predictor.plot_price_forecast(city, min_sq_meters, max_sq_meters, rooms, floor)
    click.echo("Wykres został zapisany.")


if __name__ == "__main__":
    cli()
