from dataclasses import dataclass
from datetime import date

@dataclass
class Sorozat:
    datum: date | str
    cim: str
    epizod: str
    hossz: int
    nezett: bool


sorozatok: list[Sorozat] = list()

def feladat1() -> None:
    with open("../forras/lista.txt", "r", encoding="utf-8") as forras:
        s: list[str] = list()
        for sor in forras:
            s.append(sor.strip())
            if len(s) == 5:
                if s[0] != "NI":
                    ev: int = int(s[0][0:4])
                    honap: int = int(s[0][5:7])
                    nap: int = int(s[0][8:10])
                datum: date | str = s[0] if s[0] == "NI" else date(ev, honap, nap)
                cim: str = s[1]
                epizod: str = s[2]
                hossz: int = int(s[3])
                nezett: bool = bool(int(s[4]))
                sorozatok.append(Sorozat(datum, cim, epizod, hossz, nezett))
                s.clear()


def feladat2() -> None:
    print("2. feladat")
    osszesen: int = 0
    for sorozat in sorozatok:
        if sorozat.datum != "NI":
            osszesen += 1
    print(f"A listában {osszesen} db vetítési dátummal rendelkező epizód van.")


def feladat3() -> None:
    print("3. feladat")
    megnezett_db: int = 0
    for sorozat in sorozatok:
        if sorozat.nezett:
            megnezett_db += 1
    print(f"A listában lévő epizódok {((megnezett_db / len(sorozatok))*100):0.2f}%-át látta.")


def feladat4() -> None:
    print("4. feladat")
    osszesen: int = 0
    for sorozat in sorozatok:
        if sorozat.nezett:
            osszesen += sorozat.hossz
    nap: int = osszesen // (24 * 60)
    osszesen -= nap * 24 * 60
    ora: int = osszesen // 60
    osszesen -= ora * 60
    perc = osszesen
    print(f"Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.")


def feladat5() -> None:
    print("5. feladat")
    # datum_be: str = input("Adjon meg egy dátumot! Dátum= ")
    datum_be: str = "2017.10.18"
    d = datum_be.split(".")
    datum: date = date(int(d[0]), int(d[1]), int(d[2]))
    for sorozat in sorozatok:
        if not sorozat.nezett:
            if type(sorozat.datum) == date and sorozat.datum <= datum:
                print(f"{sorozat.epizod}\t{sorozat.cim}")


def hetnapja(ev: int, ho: int, nap: int) -> str:
    napok: list[str] = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok: list[int] = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev -= 1
    return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho - 1] + nap) % 7]


def feladat7() -> None:
    print("7. feladat")
    # vizsgalt_nap: str = input("Adja meg a hét egy napját (például cs)! Nap= ")
    vizsgalt_nap: str = "cs"
    cimek: set[str] = set()
    for sorozat in sorozatok:
        if sorozat.datum != "NI":
            nap = hetnapja(sorozat.datum.year, sorozat.datum.month, sorozat.datum.day)
            if vizsgalt_nap == nap:
                cimek.add(sorozat.cim)
    if len(cimek) > 0:
        for cim in cimek:
            print(cim)
    else:
        print("Az adott napon nem kerül adásba sorozat.")


def feladat8() -> None:
    with open("summa.txt", "w", encoding="utf-8") as summa:
        i: int = 0
        while i < len(sorozatok) - 1:
            cim = sorozatok[i].cim
            osszes_ido: int = sorozatok[i].hossz
            epizodok_szama: int = 1
            innentol: int = i + 1
            for j in range(innentol, len(sorozatok)):
                if sorozatok[j].cim == cim:
                    osszes_ido += sorozatok[j].hossz
                    epizodok_szama += 1
                else:
                    summa.write(f"{cim} {osszes_ido} {epizodok_szama}\n")
                    i = j
                    break


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat7()
    feladat8()


if __name__ == '__main__':
    main()
