def main() -> None:
    szamok = [4, 1, 3, 2]
    print("1. példa:")
    rendezett_szamok = sorted(szamok)
    print(rendezett_szamok)
    print("2. példa:")
    rendezett_szamok = sorted(szamok, reverse=True)
    print(rendezett_szamok)


if __name__ == "__main__":
    main()
