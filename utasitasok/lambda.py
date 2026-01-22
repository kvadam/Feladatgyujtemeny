from functools import reduce

def main() -> None:
    szamok: list[int] = list(range(1, 11))
    print(f"Számsorozat: {szamok}")

    print("1. példa")

    paritas = lambda x: True if x % 2 == 0 else False
    if paritas(szamok[8]):
        print(f"A(z) {szamok[8]} páros szám.")
    else:
        print(f"A(z) {szamok[8]} páratlan szám.")

    print("2. példa")

    negyzet: list[int] = list(map(lambda x: x ** 2, szamok))
    print(negyzet)

    print("3. példa")
    paratlanok: list[int] = list(filter(lambda x: x % 2 == 1, szamok))
    print(paratlanok)

    print("4. példa")

    osszeg = reduce(lambda x, y: x + y, szamok)
    print(osszeg)



if __name__ == '__main__':
    main()
