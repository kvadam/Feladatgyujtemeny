from dataclasses import dataclass

@dataclass
class Telek:
    adoszam: int
    utca: str
    hazszam: str
    adosav: str
    alapter: int


fizetendo_savonkent: dict[str, int] = dict()
telkek: list[Telek] = list()

def feladat1() -> None:
    with open("../forras/utca.txt", "r", encoding="utf-8") as forras:
        adok: list[int] = [int(szam) for szam in forras.readline().strip().split(" ")]
        fizetendo_savonkent["A"] = adok[0]
        fizetendo_savonkent["B"] = adok[1]
        fizetendo_savonkent["C"] = adok[2]
        for sor in forras:
            s: list[str] = sor.strip().split(" ")
            telkek.append(Telek(int(s[0]), s[1], s[2], s[3], int(s[4])))


def feladat2() -> None:
    print(f"2. feladat. A mintában {len(telkek)} telek szerepel.")


def feladat3() -> None:
    # adoszam: int = int(input("3. feladat. Egy tulajdonos adószáma: "))
    adoszam: int = 68396
    van_epitmenye: bool = False
    for telek in telkek:
        if telek.adoszam == adoszam:
            print(f"{telek.utca} {telek.hazszam}")
            van_epitmenye = True
    if not van_epitmenye:
        print("Nem szerepel az adatállományban.")


def ado(adosav: str, alapterulet: int) -> int:
    return 0 if fizetendo_savonkent[adosav] * alapterulet < 10000 else fizetendo_savonkent[adosav] * alapterulet


def feladat5() -> None:
    print("5. feladat")
    statisztika: dict[str, list[int]] = {"A": [0, 0], "B": [0, 0], "C": [0, 0]}
    for telek in telkek:
        statisztika[telek.adosav][0] += 1
        statisztika[telek.adosav][1] += ado(telek.adosav, telek.alapter)
    for kulcs, ertekek in statisztika.items():
        print(f"{kulcs} sávba {ertekek[0]} telek esik, az adó {ertekek[1]} Ft.")


def feladat6() -> None:
    print("6. feladat. A több sávba sorolt utcák:")
    utca: str = telkek[0].utca
    savok: set[str] = set()
    for telek in telkek:
        if telek.utca != utca:
            if len(savok) > 1:
                print(utca)
            savok.clear()
            utca = telek.utca
        savok.add(telek.adosav)


def feladat7() -> None:
    with open("fizetendo.txt", "w", encoding="utf-8") as kimenet:
        tulajdonosok: set[int] = set(telek.adoszam for telek in telkek)
        fizetendo: dict[int, int] = dict()
        for telek in telkek:
            if telek.adoszam not in fizetendo.keys():
                fizetendo[telek.adoszam] = ado(telek.adosav, telek.alapter)
            else:
                fizetendo[telek.adoszam] += ado(telek.adosav, telek.alapter)
        for adoszam, osszeg in fizetendo.items():
            kimenet.write(f"{adoszam} {osszeg}\n")


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    feladat5()
    feladat6()
    feladat7()


if __name__ == '__main__':
    main()
