# zad 1

# Napisz funkcję zmien_wartosc(arg), która przyjmuje jeden argument i
# próbuje zmodyfikować ten argument w różny sposób w zależności od tego,
# czy jest on niemutowalny (w tym przypadku integerem) czy mutowalny
# (w tym przypadku listą).


def zmien_wartosc(arg):
    if isinstance(arg, int):
        arg = 65482652
    elif isinstance(arg, list):
        arg[0] = "kalafior"
    return arg


arg1 = 123
arg2 = ["abs", 2, "ksk"]
print(f"arg1:{zmien_wartosc(arg1)}\narg2:{zmien_wartosc(arg2)}\n")
print(f"arg1:{arg1}\narg2:{arg2}\n")

# Zmienna integer czyli arg1, nie zmieniła swojej wartości gdzyż jest immutable, a
# zmienna typu list, która jest mutable zmieniła już swą wartość

lista = []


def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    text = str(
        f"nazwa produktu: {nazwa_produktu}, cena: {cena * ilosc}, ilość: {ilosc}"
    )
    wartosc_zamowienia = cena * ilosc
    return text, wartosc_zamowienia


lista.append(zamowienie_produktu("kawa", cena=30, ilosc=3))
lista.append(zamowienie_produktu("arbuz", cena=30, ilosc=33))
lista.append(zamowienie_produktu("chleb", cena=10, ilosc=13))
print(lista)

for i in lista:
    print(i)

lista2 = []
for i in lista:
    lista2.append(i[1])
suma = sum(lista2)
print("Suma to:", suma)


"""
Napisz funkcję stworz_raport, która
przyjmuje dowolną liczbę argumentów pozycyjnych (*args) i nazwanych (**kwargs).
Argumenty pozycyjne powinny reprezentować numery ID produktów,
a argumenty nazwane - informacje o tych produktach (np. nazwa, cena).
Funkcja powinna tworzyć i wyświetlać raport, w którym dla każdego ID produktu
podane są szczegółowe informacje na jego temat.
"""


def stworz_raport(*args, **kwargs):
    raport = ""
    dlugosc = len(args)
    for i in range(dlugosc):
        id = args[i]
        print()
        raport += str(
            f"ID: {id}, nazwa: {kwargs[f'nazwa_{id}']}, cena: {kwargs[f'cena_{id}']}\n"
        )
    return raport


print(
    stworz_raport(
        101,
        102,
        nazwa_101="Kubek termiczny",
        cena_101="45.99 zł",
        nazwa_102="Długopis",
        cena_102="4.99 zł",
    )
)
