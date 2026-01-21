"""
    Eldöntés:

    - Minden elem vizsgálata (1. verzió):
        van_ilyen := hamis
        Ciklus sokaság minden elem-ére
            Ha elem adott tulajdonságú, akkor
                van_ilyen := igaz
            Elágazás vége
        Ciklus vége
        Ha van_ilyen, akkor
           Ki: van adott tulajdonságú elem
        Különben
           Ki: nincs adott tulajdonságú elem
        Elágazás vége


    - Csak adott tulajdonságú elem megtalálásáig keresünk (2. verzió):
        index := 0
        Ciklus amíg index < sokaság_elemszáma és NEM adott tulajdonságú sokaság[index]
            index := index + 1
        Ciklus vége
        Ha index < sokaság_elemszáma, akkor
           Ki: van adott tulajdonságú elem
        Különben
           Ki: nincs adott tulajdonságú elem
        Elágazás vége
"""

def main() -> None:
    szamok: list[int] = list(range(1, 11))
    print(f"Számsorozat: {szamok}")

    # 1. példa: Minden elem vizsgálata
    print("1. példa")

    van_paros: bool = False
    for szam in szamok:
        if szam % 2 == 0:
            van_paros = True

    if van_paros:
        print("Van páros szám a listában.")
    else:
        print("Nincs páros szám a listában.")

    # 2. példa: Csak első találatig
    print("2. példa")

    van_paros: bool = False
    for szam in szamok:
        if szam % 2 == 0:
            van_paros = True
            break

    if van_paros:
        print("Van páros szám a listában.")
    else:
        print("Nincs páros szám a listában.")

    # 3. példa: Csak első találatig while ciklussal
    print("3. példa")

    van_paros: bool = False
    i = 0
    while i < len(szamok) and not van_paros:
        if szamok[i] % 2 == 0:
            van_paros = True
        i += 1

    if van_paros:
        print("Van páros szám a listában.")
    else:
        print("Nincs páros szám a listában.")

    # 4. példa: Csak első találatig while ciklussal 2
    print("4. példa")

    i = 0
    while i < len(szamok) and szamok[i] % 2 != 0:
        i += 1

    if i < len(szamok):
        print("Van páros szám a listában.")
    else:
        print("Nincs páros szám a listában.")


if __name__ == '__main__':
    main()
