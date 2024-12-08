# 1
dane = (2024, "Python", 3.8)
rok = dane[0]
jezyk = dane[1]
wersja = dane[2]
print(f"Rok: {rok}, Jezyk: {jezyk}, wersja: {wersja}")

# 2
oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print(pierwsza, srodek, ostatnia)

# 3
info = ("Jan", "Kowalski", 30, "Polska", "programista")
imie, nazwisko, _, _, zawod = info
print(f"Imię: {imie}, Nazwisko: {nazwisko}, zawod: {zawod}")

# 4
dane = (2024, ["Python", 3.8, ("Stabilna", "Wersja")])
rok = dane[0]
jezyk = dane[1][0]
wersja = dane[1][1]
opis = dane[1][2]
print(f"Rok: {rok}, jezyk: {jezyk}, wersja: {wersja}, opis: {opis}")

# Przypisania z wieloma celami i współdzielone referencje
a = [1, 2, 3]
b1 = a
b1[0] = "zmieniono"
print(a)
print(b1)
# Każda zmienna w Pythonie to obiekt, a zmienne to tylko referencje które w naszym przypadku
# wskazują na ten sam obiekt, czyli przy modyfikacji jednej wartości w referencji b
# zmienia się też wartość dla zmiennej a

# 2
print("##########")
c = list(a)
c[0] = "nowa wartość"
print(a)
print(b1)
print(c)

# kopiowanie listy zapobiegło zmianie wartości listy a i b, podczas zmiany listy c
# ze względu na fakt, że c nie wskazuje na to samo miejsce w pamieci co zmienne a i b

# 3
x = y = 10
y = y + 1
print(x)
print(y)

# Dzieje się tak ze względu na fakt, że zmienne integer są niemutowalne, czyli podczas
# zmiany ich wartości tworzy się nowy obiekt.Sprawia to, że po dodaniu 1 do y, referencje x i y
# wskazują od tej pory na inne miejsce w pamięci, co sprawia że x nie zmienia swej wartości

# Przypisania rozszerzone i współdzielone referencje

K = [1, 2]
L = K
# konkatenacja
K = K + [3, 4]
M = [1, 2]
N = M
# przypisanie rozszerzone
M += [3, 4]
print("K:", K)
print("L:", L)
print("M:", M)
print("N:", N)


# Zawartość listy K i L różnia się ze względu na to,iż konkatenacja utworzy nowy
# obiekt K, przez co nie zostanie zmodyfikowany obiekt L
# Inaczej będzie w przypadku przypisania rozszerzonego, gdyż jest to mechanizm dzieki ktoremu
# nie zostanie utworzona nowa referencja do obiektu, czyli przez operacje +=[3,4]
# zarowno obiekt M i N zostanie zmodyfikowany.
