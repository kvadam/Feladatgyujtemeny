"""
    Kiválasztás:

    - Adott tulajdonságú elem helyének (index) megkeresése:
        index := 0
        Ciklus amíg index < sokaság_elemszáma és NEM adott tulajdonságú sokaság[index]
            index := index +1
        Ciklus vége
        Ha index < sokaság_elemszáma, akkor
            Ki: A keresett tulajdonságú elem az index+1-edik.
        különben
            Ki: Nem volt keresett tulajdonságú elem.
        Elágazás vége


"""

def main() -> None:
    szamok: list[int] = list(range(1, 11))
    szamok2: list[int] = list(range(1, 6, 2))
    print(f"Számsorozat: {szamok}")

    # 1. példa: Első páros helyének megkeresése (nem szép megoldás)
    print("1. példa")

    i: int = 0
    for szam in szamok:
        if szam % 2 == 0:
            break
        i += 1

    if i < len(szamok):
        print(f"Az első páros szám indexe: {i}")
    else:
        print("Nem volt páros szám.")

    # 2. példa: Csak első találatig while ciklussal
    print("3. példa")

    j: int = 0
    while j < len(szamok) and szamok[j] % 2 != 0:
        j += 1
   
    if j < len(szamok):
        print(f"Az első páros szám indexe: {j}")
    else:
        print("Nem volt páros szám.")

    # 3. példa: Nem tiszta implementáció
    index = None
    for k in range(len(szamok)):
        if szamok[k] % 2 == 0:
            index = k
            break

    if index:
        print(f"Az első páros szám indexe: {index}")
    else:
        print("Nem volt páros szám.")

if __name__ == '__main__':
    main()
