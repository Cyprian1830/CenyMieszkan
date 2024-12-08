# Pętle z licznikami

for i in range(6):
    print(f" Licznik: {i}")

# Skanowanie sekwencji

owoce = ["jabłko", "banan", "pomarańcza"]
for owoc in owoce:
    print(owoc)

# Przetasowanie sekwencji
# range(len(x)) iteruje po indeksach sekwencji.
# Może być użyte do manipulacji elementami na podstawie ich indeksów.

owoce = ["jabłko", "banan", "pomarańcza"]
for i in range(len(owoce)):
    owoce[i] = owoce[i].upper()
print(owoce)


# Przechodzenie niewyczerpujące
liczby = [1, 2, 3, 4, 5, 6]
for i in range(0, len(liczby), 2):
    print(liczby[i])

# Alternatywnie, z użyciem slicing
print(liczby[::2])

# Listy składane
liczby = [1, 2, 3, 4, 5, 6]
parzystosc = ["parzysta" if liczba % 2 == 0 else "nieparzysta" for liczba in liczby]
print(parzystosc)

# Przechodzenie równoległe

imiona = ["Anna", "Jan", "Piotr"]
wieki = [25, 30, 35]
for imie, wiek in zip(imiona, wieki):
    print(f"{imie} ma {wiek} lat")


def kwadrat(liczba):
    return liczba**2


liczby = [1, 2, 3, 4]
kwadraty = list(map(kwadrat, liczby))
print(kwadraty)

# zad 1

"""
Mając dwie listy, imiona = ['Anna', 'Jan', 'Ewa'] i oceny = [5, 4, 3],
użyj zip do stworzenia pary każdego imienia z odpowiadającą mu oceną.
Następnie, iteruj przez te pary, wyświetlając imię wraz z oceną.
Co się stanie, jeśli listy będą miały różne długości?
"""
imiona = ["Anna", "Jan", "Ewa", "Ala"]
oceny = [5, 4, 3]

para = list(zip(imiona, oceny))
print(para)

for imie, ocena in zip(imiona, oceny):
    print(f"{imie} dostala ocene: {ocena}")

# W momencie w którym np. lista imion jest dłuższa od listy ocen podczas iteracji
# ostatnie imie zostanie pominiete(ogolnie rzecz biorąc ostatnia para imie, ocena
# zostanie pominięte ze względu na brak oceny)

# zad 2
# Mając listę liczby = [1, 2, 3, 4, 5], napisz funkcję kwadrat(x),
# która zwraca kwadrat liczby x. Użyj map z tą funkcją,
# aby stworzyć nową listę, w której każdy element jest kwadratem
# odpowiadającego mu elementu z listy liczby. Wyświetl tą listę.

liczby = [1, 2, 3, 4, 5]


kwadratowe_liczby = list(map(kwadrat, liczby))
print(kwadratowe_liczby)


# Iteratory
liczby = [1, 2, 3]
it = iter(liczby)
print(next(it))
print(next(it))
print(next(it))
print("##################")
# Zadanie dodatkowe


class FibonacciIterator:
    def __init__(self, max_elements):
        self.max_elements = max_elements
        self.index = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # Iterator zwraca sam siebie

    def __next__(self):
        if self.index >= self.max_elements:
            raise StopIteration
        # Zatrzymanie iteracji, gdy limit zostanie przekroczony

        fib_number = self.a
        self.a, self.b = (
            self.b,
            self.a + self.b,
        )  # Aktualizuje wartości dla kolejnych wyrazów
        self.index += 1
        return fib_number


fib_iterator = FibonacciIterator(10)
# Przykładowo: generuje 10 elementów ciągu Fibonacciego
for num in fib_iterator:
    print(num)
