from datetime import datetime
import importlib
import time
aktualny_czas = datetime.now()
print(aktualny_czas)
time.sleep(5)
print(aktualny_czas)
aktualny_czas = datetime.now()
print(aktualny_czas)

# wartość zmiennej aktualny_czas zmieniła się tylko, po
# przeładowaniu pakietu time. Zmienna aktualny_czas jest
# inicjowana na samym początku wykonywania programu przez
# co nie zauważamy zmiany po uśpieniu na 5s.


