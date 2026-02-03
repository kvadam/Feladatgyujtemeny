def main() -> None:
    szamok = [1, 2, 3, 4]
    print("1. példa:")
    osszeg = sum(szamok)
    print(osszeg)
    print("2. példa:")
    osszeg = sum(szamok, 1)
    print(osszeg)
    print("3. feladat")
    d = {'a': 2, 'b': 3, 'c': 5}
    print(sum(d.values()))
    s = {1, 2, 3, 4, 5}
    print(sum(s))


if __name__ == "__main__":
    main()
