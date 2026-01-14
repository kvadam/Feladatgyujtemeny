def main() -> None:
    # Sortörés
    print()
    # Szöveg kiíratása
    print("2. Tetszőleges ékezetes szöveg.")
    # A szöveg végén elhelyezett szóközzel tagolhatunk
    print("3. Darabszám: ")
    # Idézőjelek megjelenítése szövegen belül
    print('4. Ez egy "Idézet".')
    # Tabulátorok a szövegben
    print("5. Ár\t500Ft\tÁFA\t27%")
    # Sortörés a szövegben
    print("6. Első sor\nMásodik sor")
    # Több string kiíratása egyben
    print("7.", "35", "36", "37")
    # Szeparátor és sorvége stringek beállítása (akár külön-külön is)
    print("8.", "35", "36", "37", sep="\t", end="\n")

    print("Változók kiíratása:")
    db = 5
    print(db)
    print("Darabszám:", db)
    print(f"Darabszám: {db}")

    print("Listák kiíratása")
    eladasok_lista = [5, 9, 6]
    print(eladasok_lista)

    print("Szótárak kiíratása")
    eladasok_szotar = {1: 5, 2: 9, 3: 6}
    print(eladasok_szotar)


if __name__ == "__main__":
    main()
