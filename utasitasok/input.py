def main() -> None:
    szamok: list[int] = list(range(1, 11))
    print(f"Számsorozat: {szamok}")

    print("1. példa")

    nev: str = input("Írj be egy keresztnevet: ")
    print(nev)

    print("2. példa")

    egesz: int = int(input("Írj be egy egész számot: "))
    print(egesz)

    print("3. példa")

    tizedes: float = float(input("Írj be egy tizedestörtet: "))
    print(tizedes)


if __name__ == '__main__':
    main()
