# 📊 CenaMieszkan – Analiza i Prognoza Cen Mieszkań

CenaMieszkan to projekt do analizy rynku nieruchomości, który umożliwia:  
✅ Pobieranie danych o mieszkaniach  
✅ Przetwarzanie i czyszczenie danych  
✅ Analizę statystyczną i wizualizację danych  
✅ Prognozowanie cen mieszkań w przyszłości  

Na wstępie należy stworzyć środowisko:
-make env

Do wywołania odpowiednich funkcji można się podsłużyć przykładami:

flats general-process - pobierze dane z bazy i je oczyści

flats analysis-and-visualization -  To obliczy statystyki i wygeneruje wykresy.

flats price-analysis Warszawa 30 80 -  To sprawdzi zależność ceny od metrażu w Warszawie dla mieszkań o powierzchni np. 30-80 m².
 
flats predict-price Warszawa 30 80 2 5 2030 - To przewidzi średnią cenę mieszkań w Warszawie 

flats run-forecast Gdańsk 35 90 3 1 - wykona prognoze cen np. w Gdańsku do 2050 r.
