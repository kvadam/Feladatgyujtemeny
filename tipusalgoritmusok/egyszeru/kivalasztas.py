"""
    Kiválasztás:

    - Adott tulajdonságú elem helyének (index) megkeresése:
        index := 0
        Ciklus amíg sokaság[index] NEM adott tulajdonságú
            index := index +1
        Ciklus vége
"""

def main() -> None:
    szamok: list[int] = list(range(1, 11))
    print(f"Számsorozat: {szamok}")

    # 1. példa: Első páros helyének megkeresése (nem szép megoldás)
    print("1. példa")

    i: int = 0
    for szam in szamok:
        if szam % 2 == 0:
            break
        i += 1

    print(f"Az első páros szám indexe: {i}")

    # 2. példa: Csak első találatig (nem jó megoldás)
    print("2. példa")

    for j in range(len(szamok)):
        if szamok[j] % 2 == 0:
            break

    print(f"Az első páros szám indexe: {j}")

    # 3. példa: Csak első találatig while ciklussal
    print("3. példa")

    k: int = 0
    while k < len(szamok) and szamok[k] % 2 != 0:
        k += 1

    print(f"Az első páros szám indexe: {k}")


if __name__ == '__main__':
    main()
