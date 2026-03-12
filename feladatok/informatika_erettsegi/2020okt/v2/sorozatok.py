from dataclasses import dataclass
from datetime import date

@dataclass
class Sorozat:
    datum: date
    cim: str
    epizod: str
    hossz: int
    nezett: bool


sorozatok: list[Sorozat] = list()

def str_to_date(datum_str: str) -> date:
    d = datum_str.split(".")
    ev: int = int(d[0])
    honap: int = int(d[1])
    nap: int = int(d[2])
    return date(ev, honap, nap)


def feladat1() -> None:
    with open("../forras/lista.txt", "r", encoding="utf-8") as forras:
        s: list[str] = list()
        for sor in forras:
            s.append(sor.strip())
            if len(s) == 5:
                datum: date = date(2200, 1, 1) if s[0] == "NI" else str_to_date(s[0])
                cim: str = s[1]
                epizod: str = s[2]
                hossz: int = int(s[3])
                nezett: bool = bool(int(s[4]))
                sorozatok.append(Sorozat(datum, cim, epizod, hossz, nezett))
                s.clear()


def feladat2() -> None:
    print("2. feladat")
    osszesen: int = sum([1 for sorozat in sorozatok if sorozat.datum < date(2200, 1, 1)])
    print(f"A listában {osszesen} db vetítési dátummal rendelkező epizód van.")


def feladat3() -> None:
    print("3. feladat")
    megnezett_db: int = sum([1 for sorozat in sorozatok if sorozat.nezett])
    print(f"A listában lévő epizódok {((megnezett_db / len(sorozatok))*100):0.2f}%-át látta.")


def feladat4() -> None:
    print("4. feladat")
    ossz: int = sum([sorozat.hossz for sorozat in sorozatok if sorozat.nezett])
    print(f"Sorozatnézéssel {ossz // 1440} napot {(ossz % 1440) // 60} órát és {ossz % 60} percet töltött.")


def feladat5() -> None:
    print("5. feladat")
    # be_datum: str = input("Adjon meg egy dátumot! Dátum= ")
    be_datum: str = "2017.10.18"
    datum: date = str_to_date(be_datum)
    [print(f"{sorozat.epizod}\t{sorozat.cim}") for sorozat in sorozatok if not sorozat.nezett and sorozat.datum <= datum]


def hetnapja(ev: int, ho: int, nap: int) -> str:
    napok: list[str] = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok: list[int] = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    ev = ev - 1 if ho < 3 else ev
    return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho - 1] + nap) % 7]


def feladat7() -> None:
    print("7. feladat")
    # vizsgalt_nap: str = input("Adja meg a hét egy napját (például cs)! Nap= ")
    vizsgalt_nap: str = "cs"
    cimek: set[str] = set()
    for sorozat in sorozatok:
        if sorozat.datum < date(2200, 1, 1):
            nap = hetnapja(sorozat.datum.year, sorozat.datum.month, sorozat.datum.day)
            if vizsgalt_nap == nap:
                cimek.add(sorozat.cim)
    [print(cim) for cim in cimek] if len(cimek) > 0 else print("Az adott napon nem kerül adásba sorozat.")


def feladat8() -> None:
    with open("summa.txt", "w", encoding="utf-8") as summa:
        cim: str = sorozatok[0].cim
        osszes_ido: int = 0
        epizodok_szama: int = 0
        for sorozat in sorozatok:
            if sorozat.cim == cim:
                osszes_ido += sorozat.hossz
                epizodok_szama += 1
            else:
                summa.write(f"{cim} {osszes_ido} {epizodok_szama}\n")
                cim = sorozat.cim
                osszes_ido = 0
                epizodok_szama = 0


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
