"""
    Sorozatszámítás:

    - Összegzés:
        összeg := 0
        számsorozat := 1, 10, 9 ...
        Ciklus számsorozat minden elem-ére
            összeg = összeg + elem
        Ciklus vége

    - Átlagolás:
        összeg := 0
        darab := 0
        számsorozat := 1, 10, 9 ...
        Ciklus számsorozat minden elem-ére
            összeg := összeg + elem
            darab := darab + 1
        Ciklus vége
        átlag := összeg / darab
"""

def main() -> None:
    szamok: list[int] = list(range(1, 11))
    print(f"Számsorozat: {szamok}")

    # 1. példa: összegzés
    osszeg: int = 0
    for szam in szamok:
        osszeg += szam
    print(f"Összegzés eredménye: {osszeg}")

    # 2. példa: átlagolás
    osszeg: int = 0
    darab: int = 0
    for szam in szamok:
        osszeg += szam
        darab += 1
    atlag = osszeg / darab
    print(f"Átlagolás eredménye: {atlag:.2f}")


if __name__ == '__main__':
    main()
