def main() -> None:
    szamok: list[int] = list(range(1, 11))
    print(f"Számsorozat: {szamok}")

    print("1. példa")

    if szamok[8] > 0:
        print("A szám pozitív.")

    print("2. példa")

    if szamok[8] > 0:
        print("A szám pozitív.")
    else:
        print("A szám negatív.")

    print("3. példa")

    if szamok[8] == 0:
        print("A szám nulla.")
    elif szamok[8] > 5:
        print("A szám pozitív.")
    else:
        print("A szám negatív.")


if __name__ == '__main__':
    main()
