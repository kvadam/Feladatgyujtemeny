def udv() -> None:
    print("Helló!")


def udv2(nev: str) -> None:
    print(f"Helló, {nev}!")


def udv3(nev: str) -> str:
    return f"Helló, {nev}!"


def main() -> None:
    udv()
    udv2("Péter")
    print(udv3("Laci"))


if __name__ == '__main__':
    main()
