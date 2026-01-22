def main() -> None:
    szamok: list[int] = list(range(1, 4))
    print(f"Számsorozat: {szamok}")

    print("1. példa")

    for _ in range(3):
        print("Hurrá!!!")

    print("2. példa")

    for i in range(len(szamok)):
        print(szamok[i])

    print("3. példa")

    for szam in szamok:
        print(szam)


if __name__ == '__main__':
    main()
