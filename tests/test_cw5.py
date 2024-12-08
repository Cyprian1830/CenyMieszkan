from src.zajecia05.wyjatki import *

dostepne_miejsca1 = {"a1": "wolne", "b2": "wolne", "c5": "wolne", "d7": "wolne"}
obiekt = Seans(dostepne_miejsca1)

obiekt.klienci.append(Person("Cyprian", "Szot"))
print(obiekt)

try:
    assert "zajete" not in obiekt.miejsca.values(), "Nie ma wolnych miejsc!"
except Exception as e:
    print(f"Błąd: {e}")

miejsce_1 = "a1"
try:
    assert obiekt.get_miejsce(miejsce_1) == "wolne", "To miejsce jest zarezerwowane!"
except Exception as e:
    print(f"Błąd: {e}")

klient = Person("Cyprian", "Tymoteusz")
try:
    if klient in obiekt.klienci:
        raise Exception("Ten klient już zarezerował miejsce!")
    else:
        miejsce = obiekt.zarezerwuj(miejsce_1, klient)
        obiekt.klienci.append(klient)
        print(
            f"Test: Klient {klient.name} {klient.surname} zarezerwował miejsce {miejsce_1} - OK."
        )
except Exception as e:
    print(f"blad: {e}")

print(obiekt)
try:
    if (
        miejsce_1 in obiekt.miejsca
        and obiekt.miejsca[miejsce_1] == "zajete"
        and klient in obiekt.klienci
    ):
        obiekt.zrezygnuj_z_rezerwacji("a1", klient)
        print(
            f"Test: Klient {klient.name} {klient.surname} zrezygnował z rezerwacji miejsca {miejsce_1} - OK."
        )
    else:
        raise Exception("Nie mozna dokonac anulacji rezerwacji!")
except Exception as e:
    print(f"Blad: {e}")

    # Test 4: Weryfikacja rezygnacji z rezerwacji
    try:
        if (
            miejsce_1 in obiekt.miejsca
            and obiekt.miejsca[miejsce_1] == "zajete"
            and klient in obiekt.klienci
        ):
            obiekt.zrezygnuj_z_rezerwacji(miejsce_1, klient)
            print(
                f"Test: Klient {klient.name} {klient.surname} zrezygnował z rezerwacji miejsca {miejsce_1} - OK."
            )
        else:
            raise Exception("Nie można dokonać anulacji rezerwacji!")
    except Exception as e:
        print(f"Test 4: Błąd - {e}")


print(obiekt)
