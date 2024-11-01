#Masz daną listę słowników reprezentujących informacje o książkach w bibliotece.
# Każdy słownik zawiera klucze: tytul, autor oraz rok_wydania. Twoim zadaniem jest napisanie kodu,
# który wykonuje następujące operacje przy użyciu funkcji lambda:

# zadania

dict1 = {'tytul': "Ksiazka1", 'autor': "Klemens Murański", 'rok_wydania': 1980}
dict2 = {'tytul': "Ksiazka2", 'autor': "Andrzej Murański", 'rok_wydania': 1978}
dict3 = {'tytul': "Ksiazka3", 'autor': "Krzysztof Murański", 'rok_wydania': 2001}
lista = [dict1, dict2, dict3]
print("Lista ksiazek:", lista)

rok_sorted = sorted(lista, key=lambda x: x["rok_wydania"])
print("Lista książek według roku wydania:", rok_sorted)

rok_filter_above_2000 = list(filter(lambda x: x["rok_wydania"] > 2000, lista))
print("Książki wydane po 2000: ", rok_filter_above_2000)

tylko_tytuly = list(map(lambda x: x['tytul'], lista))
print("Tylko tytuły ksiazek: ", tylko_tytuly)


# Generatory

# Napisz generator, który iteracyjnie zwraca nazwy dni tygodnia: od poniedziałku do niedzieli.
# Następnie, użyj tego generatora w pętli, aby wyświetlić każdy dzień tygodnia.
# Dodatkowo, zademonstruj, jak można użyć tego generatora do pobrania tylko pierwszych trzech dni tygodnia
# bez konieczności iterowania przez cały tydzień.


dni_tygodnia = ["Poniedzialek", "Wtorek", "Sroda", "Czwartek", "Piatek", "Sobota", "Niedziela"]
generator_1 = (x for x in dni_tygodnia)

for i in generator_1:
    print(i)

# pon = (next(generator_1))
# wt = (next(generator_1))
# sr = (next(generator_1))

# trzy_dni = [pon, wt, sr]
# print(trzy_dni)



def dni_tygodnia_fun(lista: list) -> str:
    count = 0
    while count <= len(lista):
        yield lista[count]
        count += 1

print( "#################### ")
tydzien = dni_tygodnia_fun(dni_tygodnia)

print(next(tydzien))
print(next(tydzien))
print(next(tydzien))