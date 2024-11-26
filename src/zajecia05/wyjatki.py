dostepne_miejsca1 = {"a1": "wolne", "b2": "wolne", "c5": "wolne", "d7": "wolne"}


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    #def __str__(self):
     #   return f"Imie: {self.name}, Nazwisko: {self.surname}"

    def __eq__(self, other):
        if isinstance(other, Person):
            return (self.name == other.name and self.surname == other.surname)
        return False

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __hash__(self):
        return hash((self.name, self.surname))  # Tworzymy hash aby nie bylo blad: unhashable type 'Person'


class Seans:
    def __init__(self, dostepne_miejsca: dict,):
        self.miejsca = dostepne_miejsca
        self.klienci: Person = []

    def set_klienci(self, klienci):
        self.klienci = klienci

    def get_klienci(self):
        return self.klienci

    def set_miejsca(self, miejsca):
        self.miejsca=miejsca

    def get_miejsce(self, miejsce):
        return self.miejsca[miejsce]

    def zarezerwuj(self, miejsce, uzytkownik:Person):
        zarezerwowane_miejsce=self.miejsca.pop(miejsce)
        print(f'Zarezerwowane miejsce to: {miejsce} przez klienta:  {uzytkownik}')
        self.miejsca[miejsce] = "zajete"

        return zarezerwowane_miejsce

    def zrezygnuj_z_rezerwacji(self, miejsce, uzykownik: Person):
        self.miejsca[miejsce] = "wolne"
        self.klienci.remove(uzykownik)

    def __str__(self):
        klienci_str = ", ".join(str(klient) for klient in self.klienci)  # Zamiana obiektów na stringi
        return f'Wolne miejsca: {self.miejsca} Klienci: {klienci_str}'

obiekt = Seans(dostepne_miejsca1)

obiekt.klienci.append(Person("Cyprian", "Szot"))
print(obiekt)

try:
    if "wolne" not in obiekt.miejsca.values():
        raise Exception("There is no more seats!")
except Exception as e:
    print(f"Błąd: {e}")

miejsce_1 = "a1"
try:
    if obiekt.get_miejsce(miejsce_1) == "zajete":
        raise Exception("To miejsce jest zarezerwowane")
except Exception as e:
    print(f"Błąd: {e}")

klient = Person("Cyprian", "Tymoteusz")
try:
    if klient in obiekt.klienci:
        raise Exception("Ten klient już zarezerował miejsce!")
    else:
        miejsce = obiekt.zarezerwuj(miejsce_1, klient)
        obiekt.klienci.append(klient)
except Exception as e:
    print(f"blad: {e}")

print(obiekt)
try:
    if miejsce_1 in obiekt.miejsca and obiekt.miejsca[miejsce_1] == "zajete" and klient in obiekt.klienci:
        obiekt.zrezygnuj_z_rezerwacji("a1", klient)
    else:
        raise Exception("Nie mozna dokonac anulacji rezerwacji!")
except Exception as e:
    print(f"Blad: {e}")

print(obiekt)








