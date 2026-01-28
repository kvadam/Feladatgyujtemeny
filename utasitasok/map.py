def negyzet(x: int) -> int:
    return x ** 2


def main() -> None:
    szamok: list[int] = list(range(1, 11))
    print(f"Számsorozat: {szamok}")

    print("1. példa")

    negyzetek: list[int] = list(map(negyzet, szamok))
    print(negyzetek)

    print("2. példa")

    negyzetek2: list[int] = list(map(lambda x: x ** 2, szamok))
    print(negyzetek2)


if __name__ == '__main__':
    main()
