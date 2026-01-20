from dataclasses import dataclass

@dataclass()
class Csomopont:
        meter: int
        megnevezes: str


adatok: list[Csomopont] = list()

def varosnev_e(megnevezes: str) -> bool:
    if len(megnevezes) > 2:
        return True
    return False


def feladat1() -> int:
    with open("../forras/ut.txt", "r", encoding="utf-8") as forras:
        hossz = int(forras.readline().strip())
        for sor in forras:
            s = sor.strip().split(" ")
            adat = Csomopont(int(s[0]), s[1])
            adatok.append(adat)
    return hossz


def feladat2() -> None:
    print("2. feladat")
    print("A települések neve:")
    for csomopont in adatok:
        if varosnev_e(csomopont.megnevezes):
            print(csomopont.megnevezes)


def feladat3() -> None:
    print("3. feladat")
    # vizsgalt_hossz = float(input("Adja meg a vizsgált szakasz hosszát km-ben! "))
    vizsgalt_hossz = 1.8
    min_sebesseg = 90
    for csomopont in adatok:
        if csomopont.meter > vizsgalt_hossz * 1_000:
            break
        if str.isdigit(csomopont.megnevezes):
            min_sebesseg = min(min_sebesseg, int(csomopont.megnevezes))
        elif varosnev_e(csomopont.megnevezes):
            min_sebesseg = min(min_sebesseg, 50)

    print(f"Az első {vizsgalt_hossz} km-en {min_sebesseg} km/h volt a legalacsonyabb megengedett sebesség.")


def feladat4(ut_hossza: int) -> None:
    print("4. feladat")
    ut_varosban_osszesen = 0
    varos_metertol = 0
    for csomopont in adatok:
        if varosnev_e(csomopont.megnevezes):
            varos_metertol = csomopont.meter
        elif csomopont.megnevezes == "]":
            ut_varosban = csomopont.meter - varos_metertol
            ut_varosban_osszesen += ut_varosban

    print(f"Az {(ut_varosban_osszesen / ut_hossza) * 100:0.2f} százaléka vezet településen belül.")


def feladat5() -> str:
    print("5. feladat")
    # telepules = input("Adja meg egy település nevét! ")
    telepules = "Varos010"
    varosban = False
    varos_metertol = 0
    tablak_szama = 0
    ut_varosban = 0
    for csomopont in adatok:
        if not varosban and varosnev_e(csomopont.megnevezes):
            if csomopont.megnevezes == telepules:
                varosban = True
                varos_metertol = csomopont.meter
                continue
        if varosban:
            if str.isdigit(csomopont.megnevezes):
                tablak_szama += 1
            elif csomopont.megnevezes == "]":
                ut_varosban = csomopont.meter - varos_metertol
                break

    print(f"A sebességkorlátozó táblák száma: {tablak_szama}")
    print(f"Az út hossza a településen belül {ut_varosban} méter.")
    return telepules


def feladat6(telepules: str) -> None:
    ti = 0
    kov_varos_index = -1
    elozo_varos_index = -1
    legkozelebbi_varos_index = -1

    for i in range(len(adatok)):
        if varosnev_e(adatok[i].megnevezes):
            if adatok[i].megnevezes == telepules:
                ti = i
                break

    for i in range(ti + 1, len(adatok)):
        if varosnev_e(adatok[i].megnevezes):
            kov_varos_index = i
            break

    for i in range(ti - 1, -1, -1):
        if varosnev_e(adatok[i].megnevezes):
            elozo_varos_index = i
            break

    if kov_varos_index < 0:
        legkozelebbi_varos_index = elozo_varos_index
    elif elozo_varos_index < 0:
        legkozelebbi_varos_index = kov_varos_index
    elif (adatok[kov_varos_index].meter - adatok[ti].meter) < (adatok[ti].meter - adatok[elozo_varos_index].meter):
        legkozelebbi_varos_index = kov_varos_index
    else:
        legkozelebbi_varos_index = elozo_varos_index

    print(f"A legközelebbi település: {adatok[legkozelebbi_varos_index].megnevezes}")


def main():
    ut_hossza: int = feladat1()
    feladat2()
    feladat3()
    feladat4(ut_hossza)
    telepules = feladat5()
    feladat6(telepules)


if __name__ == "__main__":
    main()
