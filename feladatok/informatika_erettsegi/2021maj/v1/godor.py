from dataclasses import dataclass

@dataclass
class Godor:
    kezd: int
    veg: int
    m: list[int]

melysegek: list[int] = list()
godrok: list[Godor] = list()

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
    with open("godrok.txt", "w", encoding="utf-8") as godrok_txt:
        godor: bool = False
        godrok_szama: int = 0
        j: int = -1
        for i in range(1, len(melysegek)):
            if melysegek[i - 1] == 0 and melysegek[i] != 0:
                godor = True
                godrok_szama += 1
                godrok.append(Godor(i, -1, [melysegek[i]]))
                j += 1
            elif melysegek[i - 1] != 0 and melysegek[i] == 0:
                godor = False
                godrok[j].veg = i - 1
                godrok_txt.write("\n")
            if godor:
                godrok[j].m.append(melysegek[i])
                godrok_txt.write(f"{melysegek[i]} ")
    return godrok_szama


def feladat5(godrok_szama: int) -> None:
    print("5. feladat")
    print(f"A gödrök száma: {len(godrok)}")


def melyik_godor(tav: int) -> int:
    i: int = 0
    while i < len(godrok) and not (godrok[i].kezd < tav and godrok[i].veg > tav):
        i += 1

    if i < len(godrok):
        return i
    else:
        return -1


def feladat6(tavolsag: int) -> None:
    print("6. feladat")
    print("a)")
    gi: int = melyik_godor(tavolsag)
    print(f"A gödör kezdete: {godrok[gi].kezd + 1} méter, a gödör vége: {godrok[gi].veg + 1} méter.")
    print("b)")
    i: int = 0
    j: int = len(godrok[gi].m) - 1
    while i < j and godrok[gi].m[i] >= godrok[gi].m[i - 1] and godrok[gi].m[j] >= godrok[gi].m[j + 1]:
        i += 1
        j -= 1
    if i < j:
        print("Nem mélyül folyamatosan.")
    else:
        print("Folyamatosan mélyül.")
    print("c)")
    max_melyseg: int = melysegek[godrok[gi].kezd]
    i = godrok[gi].kezd + 1
    while i < len(godrok[gi].m):
        if godrok[gi].m[i] > max_melyseg:
            max_melyseg = godrok[gi].m[i]
        i += 1
    print(f"A legnagyobb mélysége {max_melyseg} méter.")
    print("d)")
    v: int = 0
    i = godrok[gi].kezd
    while i < len(godrok[gi].m):
        v += melysegek[i] * 10
        i += 1
    print(f"A térfogata {v} m^3.")
    print("e)")
    vv: int = v - ((godrok[gi].veg - (godrok[gi].kezd - 1)) * 10)
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
