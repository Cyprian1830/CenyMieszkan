import time


def dekorator1(unit):
    if unit not in ["microseconds", "seconds"]:
        return

    def dekorator(funkcja):
        def wrapper(*args):
            czas1 = time.time()
            print("Czas na starcie: ", czas1)
            funkcja(*args)
            czas2 = time.time()
            res = czas2 - czas1
            print("Czas na końcu: ", czas2)
            if unit == "microseconds":
                res *= 1000000
            print("Czas wykonania funkcji to: ", res)
            return res

        return wrapper

    return dekorator


@dekorator1("seconds")
def moja_funkcja(n):
    for i in range(n):
        print(i)


moja_funkcja(1000)
