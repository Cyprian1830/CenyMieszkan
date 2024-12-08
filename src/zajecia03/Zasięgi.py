# zad 1
def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return pow(podstawa, wykladnik)

    return poteguj


potega_2 = stworz_funkcje_potegujaca(2)  # Tworzy funkcję potęgującą do kwadratu
print(potega_2(4))  # Wynik: 16


# licznik zad1


def licznik():
    counter = 0

    def licznik_():
        nonlocal counter
        counter += 1
        return counter

    return licznik_


counter = 0
funkcja = licznik()
print(funkcja())
print(funkcja())
print(funkcja())

print("#############")


def licznik_2():
    """
    Jest to funkcja, któa ma za zadanie używać zmiennej globalnej i zwiększać jej wartość
    za każdym razem, gdy zostanie wywołana i dodatkowo ją zwracać.

    """
    global counter
    counter += 1
    return counter


print(licznik_2())
print(licznik_2())
print(licznik_2())

print("########")


class licznik_klasa:
    def __init__(self):
        self.counter = 0

    def dodaj(self):
        self.counter += 1
        return self.counter


obiekt = licznik_klasa()
print(obiekt.dodaj())
print(obiekt.dodaj())
print(obiekt.dodaj())
print(obiekt.dodaj())
print(obiekt.dodaj())

print("##############")


def funkcja_z_atrybutem():
    funkcja_z_atrybutem.suma += 1
    return funkcja_z_atrybutem.suma


funkcja_z_atrybutem.suma = 0
print(funkcja_z_atrybutem())
print(funkcja_z_atrybutem())
funkcja_z_atrybutem()
funkcja_z_atrybutem()
funkcja_z_atrybutem()
funkcja_z_atrybutem()
print(funkcja_z_atrybutem())
