from dataclasses import dataclass

@dataclass
class Godor:
    kezd: int
    veg: int
    melysegek: list[int]

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
    erintetlen: int = sum([1 for melyseg in melysegek if melyseg == 0])
    print(f"Az érintetlen területek aránya {((erintetlen / len(melysegek)) * 100):0.2f}%")


def feladat4() -> int:
    with open("godrok.txt", "w", encoding="utf-8") as godrok_txt:
        godor: bool = False
        j: int = -1
        for i in range(1, len(melysegek)):
            if melysegek[i - 1] == 0 and melysegek[i] != 0:
                godor = True
                godrok.append(Godor(i, -1, []))
                j += 1
            elif melysegek[i - 1] != 0 and melysegek[i] == 0:
                godor = False
                godrok[j].veg = i - 1
                godrok_txt.write("\n")
            if godor:
                godrok[j].melysegek.append(melysegek[i])
                godrok_txt.write(f"{melysegek[i]} ")
    return len(godrok)


def feladat5() -> None:
    print("5. feladat")
    print(f"A gödrök száma: {len(godrok)}")


def melyik_godor(tav: int) -> int:
    i: int = 0
    while i < len(godrok) and not (godrok[i].kezd < tav and godrok[i].veg > tav):
        i += 1

    godor_index: int = i if i < len(godrok) else -1
    return godor_index


def feladat6(tavolsag: int) -> None:
    print("6. feladat")
    gi: int = melyik_godor(tavolsag)
    if gi < 0:
        print("Az adott helyen nincs gödör.")
        return
    godor: Godor = godrok[gi]

    print("a)")
    print(f"A gödör kezdete: {godor.kezd + 1} méter, a gödör vége: {godor.veg + 1} méter.")
    # B részt ellenőrizni

    print("b)")
    melypont: int = max(godor.melysegek)
    mp_i: int = godor.melysegek.index(melypont)
    i: int = mp_i
    while i < len(godor.melysegek) and godor.melysegek[i] >= godor.melysegek[i + 1]:
        i += 1
    j: int = mp_i
    while j > 1 and godor.melysegek[j] >= godor.melysegek[j - 1]:
        j -= 1
    if i < len(godor.melysegek) and j > 0:
        print("Nem mélyül folyamatosan.")
    else:
        print("Folyamatosan mélyül.")

    print("c)")
    max_melyseg: int = max([melyseg for melyseg in godor.melysegek])
    print(f"A legnagyobb mélysége {max_melyseg} méter.")

    print("d)")
    terfogat: int = sum([melyseg * 10 for melyseg in godor.melysegek])
    print(f"A térfogata {terfogat} m^3.")

    print("e)")
    vizmennyiseg: int = terfogat - (len(godor.melysegek) * 10)
    print(f"A vízmennyiség {vizmennyiseg} m^3.")


def main() -> None:
    feladat1()
    tavolsag: int = feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6(tavolsag)


if __name__ == '__main__':
    main()
