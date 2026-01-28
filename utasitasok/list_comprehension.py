def main() -> None:
    szamok: list[int] = list(range(1, 11))
    print(f"Számsorozat: {szamok}")

    print("1. példa")

    for szam in szamok:
        print(szam, end=" ")
    print()
    # vagy
    [print(szam, end=" ") for szam in szamok]
    print()

    print("2. példa")
    paros_szamok: list[int] = list()
    for szam in szamok:
        if szam % 2 == 0:
            paros_szamok.append(szam)
    print(paros_szamok)
    # vagy
    paros_szamok2: list[int] = [szam for szam in szamok if szam % 2 == 0]
    print(paros_szamok2)

    print("3. példa")
    paros_negyzet: list[int] = list()
    for szam in szamok:
        if szam % 2 == 0:
            negyzet: int = szam ** 2
            paros_negyzet.append(negyzet)
    print(paros_negyzet)
    # vagy
    paros_negyzet2: list[int] = [szam ** 2 for szam in szamok if szam % 2 == 0]
    print(paros_negyzet2)


if __name__ == '__main__':
    main()
