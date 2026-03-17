melysegek: list[int] = list()

def feladat1() -> None:
    print("1. feladat")
    with open("../forras/melyseg.txt", "r", encoding="utf-8") as forras:
        for sor in forras:
            melysegek.append(int(sor.strip()))
        print(f"A fájl adatainak száma: {len(melysegek)}")


def feladat2() -> int:
    print("2. feladat")
    # tavolsag: int = int(input("Adjon meg egy távolságértéket! "))
    tavolsag: int = 9
    print(f"Ezen a helyen a felszín {melysegek[tavolsag - 1]} méter mélyen van")
    return tavolsag


def feladat3() -> None:
    print("3. feladat")
    erintetlen: int = 0
    for melyseg in melysegek:
        if melyseg == 0:
            erintetlen += 1
    print(f"Az érintetlen területek aránya {((erintetlen / len(melysegek)) * 100):0.2f}%")


def feladat4() -> int:
    with open("godrok.txt", "w", encoding="utf-8") as godrok:
        godor: bool = False
        godrok_szama: int = 0
        for i in range(1, len(melysegek)):
            if melysegek[i - 1] == 0 and melysegek[i] != 0:
                godor = True
                godrok_szama += 1
            elif melysegek[i - 1] != 0 and melysegek[i] == 0:
                godor = False
                godrok.write("\n")
            if godor:
                godrok.write(f"{melysegek[i]} ")
    return godrok_szama


def feladat5(godrok_szama: int) -> None:
    print("5. feladat")
    print(f"A gödrök száma: {godrok_szama}")

def feladat6(tavolsag: int) -> None:
    print("6. feladat")
    if melysegek[tavolsag - 1] == 0:
        print("Az adott helyen nincs gödör.")
        return

    print("a)")
    print(tavolsag)
    kezdopont: int = 0
    vegpont: int = 0
    i: int = tavolsag
    while melysegek[i - 1] != 0:
        i -= 1
    kezdopont = i + 1
    i = tavolsag
    while melysegek[i - 1] != 0:
        i += 1
    vegpont = i - 1
    print(f"A gödör kezdete: {kezdopont} méter, a gödör vége: {vegpont} méter.")

    print("b)")
    i = kezdopont - 1
    j: int = vegpont - 1
    while i < j and melysegek[i] >= melysegek[i - 1] and melysegek[j] >= melysegek[j + 1]:
        i += 1
        j -= 1
    if i < j:
        print("Nem mélyül folyamatosan.")
    else:
        print("Folyamatosan mélyül.")

    print("c)")
    max_melyseg: int = melysegek[kezdopont - 1]
    i = kezdopont
    while i < vegpont:
        if melysegek[i] > max_melyseg:
            max_melyseg = melysegek[i]
        i += 1
    print(f"A legnagyobb mélysége {max_melyseg} méter.")

    print("d)")
    v: int = 0
    i = kezdopont - 1
    while i < vegpont:
        v += melysegek[i] * 10
        i += 1
    print(f"A térfogata {v} m^3.")

    print("e)")
    vv: int = v - ((vegpont - (kezdopont - 1)) * 10)
    print(f"A vízmennyisé {vv} m^3.")


def main() -> None:
    feladat1()
    tavolsag: int = feladat2()
    feladat3()
    godrok_szama: int = feladat4()
    feladat5(godrok_szama)
    feladat6(tavolsag)


if __name__ == '__main__':
    main()
