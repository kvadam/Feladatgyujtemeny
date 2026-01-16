def main() -> None:
    arak: list[int] = [10, 100, 1000]
    x: int = 5
    ar: int = 5000000
    f: float = 4.567
    s = "Alma"
    # F string deklarációja
    fs: str = f"Almák száma: {x}"
    print(fs)
    # F string printben
    print(f"Ár: {x}eFt.")
    # Ezres tagolás
    print(f"{ar:,}")
    # Tört számok kiíratása és megjelenítése kerekítéssel
    print(f"Érték: {f}, kerekítve: {f:.1f}")

    # Szám kiíratása fix hosszúságon
    print(f"{x:5} szóköz hosszúság")
    # Szöveg kiíratása fix hosszúságon
    print(f"{s:=^10}")
    print(f"{s:_<10}")
    print(f"{s:>10}")
    # Megjelenítés százalékos formában
    print(f"{f:%}")
    print(f"{f:.2%}")

    # Kifejezés eredménynének behelyettesítése
    print(f"A számítás eredménye: {(x * 10) / 4}")
    print(f"A számítás eredménye: {(x * 10) / 4 = }")

    # Listaelem kiíratása
    i: int = 1
    print(f"A {i + 1}. termék ára: {arak[i]} Ft.")



if __name__ == "__main__":
    main()
