import math
from time import perf_counter

sh: int = 160
ash: int = 0

def idomero(metodus):
    def csomagolo(*args, **kwargs):
        kezd_ido = perf_counter()
        eredmeny = metodus(*args, **kwargs)
        veg_ido = perf_counter()
        print(f"\nFutási idő: {(veg_ido - kezd_ido):.4f} mp")
        return eredmeny
    return csomagolo


def printts(ertek) -> None:
    global sh
    global ash

    szoveg = ertek if type(ertek) == str else str(ertek)

    if ash + len(szoveg) > sh:
        ash = 0
        print()

    ash += len(szoveg) + 1

    print(f"{szoveg} ", end="")


@idomero
def esz(szamok: list[int], n: int) -> list[int]:
    printts("Előrehaladás:")
    i: int = 2
    while i < math.sqrt(n):
        printts(i)
        j: int = 0
        if i == szamok[j]:
            j += 1
        while j < len(szamok):
            if szamok[j] % i == 0 and i != szamok[j]:
                # printts(f"-{szamok[j]}")
                szamok.pop(j)
            j += 1
        i += 1
    return szamok


def main() -> None:
    global ash
    n: int = int(input("Add meg a keresés felső határát: "))
    szamok: list[int] = list()
    for i in range(2, n + 1):
        szamok.append(i)

    primek: list[int] = esz(szamok, n)

    print("\nPrím számok:")
    ash = 0
    for i in range(len(primek)):
        printts(primek[i])
    print(f"\n\nA prímek száma 1-{n}-ig: {len(primek)}")


if __name__ == '__main__':
    main()
