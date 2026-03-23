from dataclasses import dataclass

@dataclass
class Keppont:
    r: int
    g: int
    b: int


keppontok: list[list[Keppont]] = list()

def feladat1() -> None:
    with open("../forras/kep.txt", "r", encoding="utf-8") as forras:
        i: int = 0
        for sor in forras:
            s: list[int] = [int(szam) for szam in sor.strip().split(" ")]
            keppontok.append(list())
            for j in range(0, len(s), 3):
                keppontok[i].append(Keppont(s[j], s[j+1], s[j+2]))
            i += 1


def feladat2() -> None:
    print("2. feladat")
    print("Kérem egy képpont adatait!")
    # x: int = int(input("Sor: "))
    # y: int = int(input("Oszlop: "))
    x: int = 180
    y: int = 320
    print(f"A képpont színe RGB({keppontok[x-1][y-1].r}, {keppontok[x-1][y-1].g}, {keppontok[x-1][y-1].b})")


def feladat3() -> None:
    print("3. feladat")
    vilagos_keppontok_szama: int = 0
    for sor in keppontok:
        for keppont in sor:
            if (keppont.r + keppont.g + keppont.b) > 600:
                vilagos_keppontok_szama += 1
    print(f"A világos képpontok száma: {vilagos_keppontok_szama}")


def feladat4() -> None:
    print("4. feladat")
    legkisebb_osszeg: int = keppontok[0][0].r + keppontok[0][0].g + keppontok[0][0].b
    for sor in keppontok:
        for keppont in sor:
            osszeg: int = keppont.r + keppont.g + keppont.b
            if osszeg < legkisebb_osszeg:
                legkisebb_osszeg = osszeg
    for sor in keppontok:
        for keppont in sor:
            osszeg: int = keppont.r + keppont.g + keppont.b
            if osszeg == legkisebb_osszeg:
                print(f"RGB({keppont.r}, {keppont.g}, {keppont.b})")


def hatar(ssz: int, elteres: int) -> bool:
    van_hatar: bool = False
    # kidolgozandó
    return van_hatar


def feladat6() -> None:
    # kidolgozandó
    pass


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat6()


if __name__ == '__main__':
    main()
