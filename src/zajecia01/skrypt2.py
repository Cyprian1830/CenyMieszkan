import math
import random
import json

# Działania matematyczne

wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie**123
text = str(potega)
wartosc_pi = math.pi
losowa = random.choice([1, 2, 3, 4, 5])

# Łańcuchy znaków

text = f"Wartosc: {text}"
dlugosc = len(text)
wycinek = text[1:4]
print(dlugosc)
print(wycinek)
print(dir(text))
text = text.upper()
print(text)
# text[2] = "p"
# strings are not mutable

# Listy
lista = list(text[:8])
lista.append([1, 2, 3, 4, 5])
lista.remove(":")
print(lista)

# Listy składane (list comprehension)
print("lista: ", lista)
lista2 = [1, 2, 3, "banan", 100]
print("lista2: ", lista2)
lista3 = [x**2 for x in lista2 if x != "banan"]
print("lista3: ", lista3)
lista4 = [x for x in range(2, 17, 2)]
print("lista4: ", lista4)

# Słowniki
ja = dict(
    imie="Cyprian",
    nazwisko="Szot",
    wiek=20,
    rodzice=[{"imie": "Bogdan", "wiek": 62}, {"imie": "Ewa", "wiek": 58}],
)
print(f"Rodzice to: {ja['rodzice']}")

print(f"Imie rodzica to: {ja['rodzice'][0]['imie']}")
print(f"Wszystkie klucze w słowniku to: {ja.keys()}")
logika = "rodzenstwo" in ja
print(f"Czy nasz słownik posiada klucz rodzeństwo?: {logika}")

# Krotki
krotka1 = (1, 2, "3", 4, 2, 5)
print(f"Dlugosc: {len(krotka1)}, pierwszy wyraz: {krotka1[0]}")
ilosc2 = krotka1.count(2)
print(f"Ile razy występuje w krotce wartość 2?: {ilosc2}")
# krotka1[0] = 2
# nie można zmienić wartość pierwszej wartości w krotce ze względu na fakt, iż krotka jest obiektem immutable

# Zbiory
X = set("kalarepa")
Y = set("lepy")

print(f"Czesc wspolna: {X.intersection(Y)}")

# Instrukcje
# 1
imiona = [
    "Cyprian",
    "Kamil",
    "Amelia",
    "Agata",
    "Emilka",
    "Asia",
    "Iwo",
    "Tytus",
    "Kasia",
]
for indeks, imie in enumerate(imiona):
    print(f"Indeks: {indeks}, imię: {imie}")

# 2a


def znak_i_parzystosc(x):
    znak = "ujemna lub zerowa"
    parzystosc = "nieparzysta"
    if x > 0:
        znak = "dodatna"
    if x % 2 == 0:
        parzystosc = "parzysta"
    return f"Liczba jest {znak} i {parzystosc}"


print(znak_i_parzystosc(6))

# 2b


def czy_rowna_zero(x):
    if x != 0:
        return "Liczba jest różna od zera!!!"
    else:
        return "Liczba jest równa zero!!!"


print(czy_rowna_zero(1))

# 2c


def dostep_do_owocow(owoc):
    lista = ["jabłko", "banan", "pomarańcza"]
    wynik = owoc in lista
    if wynik:
        print("Owoc jest dostępny!")
    else:
        print("Owoc nie jest dostępny!")


dostep_do_owocow("banan")

# x = 0
# while x <= 100:
#     y = float(input("Podaj liczbę całkowitą: "))
#     x = x + y
# print(f"Suma wprowadzonych liczb to: {x}")

# Dziwactwa
# 1
L = [1, 2, 3, 4]
M = [1, 2, 3, L, 4]

print(f"Wartość zmiennej M przed zmianą L: {M}")

L[1] = "woooow"

print(f"Wartość zmiennej M po zmianie L: {M}")

# obiekt M zawiera w sobie obiekt L, który jeżeli zostanie zmodyfikowany to autoamtycznie modyfikuje się wartość M
# gdyż M zawiera referencję do obiektu L

# 2

L = [4, 5, 6]

X1 = L * 4

Y1 = [L] * 4

print(f"X: {X1}, Y: {Y1}")

L[1] = "wow"

print(f"X: {X1}, Y: {Y1}")

L = [4, 5, 6]

Y = [list(L)] * 4

L[1] = "wow"

print(f"Y: {Y1}")

Y1 = "wow"

print(f"Y: {Y1}")

print("#######################################################")
# Zadania sprawdzające
# zad 1


with open("teksty.json") as file:
    dane = json.load(file)

print(dane)
teksty2 = ""
for item in dane["teksty"]:
    for teksty in item.values():
        teksty2 += teksty + ""

print(teksty2)

print("Zamiana na duzych liter na małe:\n")
male = teksty2.lower()
print(teksty2)

print("Dzielenie na wyrazy:")
wyrazy = male.split()
print(wyrazy)

print("Bez znaków interpunkcyjnych:")
bez_znakow = [wyraz.replace(".", "").replace(",", "") for wyraz in wyrazy]
print(bez_znakow)

duze_na_koncu = [wyraz[:-1] + wyraz[-1].upper() for wyraz in bez_znakow]
print("Duze na końcu:")
print(duze_na_koncu)

print("Wyrazy gdzie występuje a lub A: ")
lista = [wyraz for wyraz in duze_na_koncu if "a" in wyraz.lower()]
print(lista)

print("Unikatowe wartości: ")
zestaw = set(lista)
print(zestaw)

slownik = dict()
for word in lista:
    counter = lista.count(word)
    slownik[word] = counter
print("Slownik: ")
print(slownik)


wyniki = {
    "Scalone ": teksty2,
    "Zmiana duzych na liter na male \n": male,
    "Podzielenie na wyrazy \n": wyrazy,
    "Bez interpunkcji \n": bez_znakow,
    "Duze na końcu \n": duze_na_koncu,
    "Wyrazy z a lub A \n": lista,
    "Unikatowe wartosci \n": list(zestaw),
    "Ilosc wystapien \n": slownik,
}


with open("wyniki.json", "w") as file:
    json.dump(wyniki, file)
