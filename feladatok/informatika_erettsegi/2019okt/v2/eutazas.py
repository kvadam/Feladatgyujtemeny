from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Felszallo:
    mid: int
    fdat: datetime
    fid: str
    berlet: str
    edat: datetime | int


felszallok: list[Felszallo] = list()

def napokszama(e1: int, h1: int, n1: int, e2: int, h2: int, n2: int) -> int:
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1= 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2= 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) // 10 + n2 - 1
    return d2-d1


def szovegbol_datum(szoveg: str) -> datetime:
    ev: int = int(szoveg[0:4])
    honap: int = int(szoveg[4:6])
    nap: int = int(szoveg[6:8])
    if len(szoveg) > 8:
        ora: int = int(szoveg[9:11])
        perc: int = int(szoveg[11:13])
        mp: int = 0
    else:
        ora: int = 23
        perc: int = 59
        mp: int = 59
    return datetime(ev, honap, nap, ora, perc, mp)


def ervenyes(f: Felszallo) -> bool:
    if type(f.edat) == int and f.edat == 0:
        return False
    if type(f.edat) == datetime and f.fdat > f.edat:
        return False
    return True


def feladat1() -> None:
    with open("../forras/utasadat.txt", "r", encoding="utf-8") as forras:
        for sor in forras:
            s: list[str] = sor.strip().split(" ")
            mid: int = int(s[0])
            fdat: datetime = szovegbol_datum(s[1])
            fid: str = s[2]
            berlet: str = s[3]
            if len(s[4]) < 8:
                edat: int = int(s[4])
            else:
                edat: datetime = szovegbol_datum(s[4])
            felszallok.append(Felszallo(mid, fdat, fid, berlet, edat))


def feladat2() -> None:
    print("2. feladat")
    print(f"A buszra {len(felszallok)} utas akart felszállni.")


def feladat3() -> None:
    print("3. feladat")
    nem_utazhat: int = sum([1 for f in felszallok if not ervenyes(f)])
    print(f"A buszra {nem_utazhat} utas nem szállhatott fel.")


def feladat4() -> None:
    megallok: dict[int, int] = {i : 0 for i in range(30)}
    for f in felszallok:
        megallok[f.mid] += 1
    maxf: int = max([v for v in megallok.values()])
    for k in megallok:
        if megallok[k] == maxf:
            print(f"A legtöbb utas ({megallok[k]} fő) a {k}. megállóban próbált felszállni.")
            return


def feladat5() -> None:
    print("5. feladat")
    ingyenes_fo: int = 0
    kedvezmenyes_fo: int = 0
    for felszallo in felszallok:
        if not ervenyes(felszallo):
            continue
        if felszallo.berlet in ["NYP", "RVS", "GYK"]:
            ingyenes_fo += 1
        if felszallo.berlet in ["TAB", "NYB"]:
            kedvezmenyes_fo += 1
    print(f"Ingyenesen utazók száma: {ingyenes_fo} fő")
    print(f"A kedvezményesen utazók száma: {kedvezmenyes_fo} fő")


def feladat7() -> None:
    with open("figyelmeztetes.txt", "w", encoding="utf-8") as kimenet:
        for felszallo in felszallok:
            if type(felszallo.edat) == datetime:
                ev1: int = felszallo.fdat.year
                ho1: int = felszallo.fdat.month
                nap1: int = felszallo.fdat.day
                ev2: int = felszallo.edat.year
                ho2: int = felszallo.edat.month
                nap2: int = felszallo.edat.day
                napok = napokszama(ev1, ho1, nap1, ev2, ho2, nap2)
                if napok >= 0 and napok <=3:
                    kimenet.write(f"{felszallo.fid}  {felszallo.edat.year}-{felszallo.edat.month}-{felszallo.edat.day}\n")


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat7()


if __name__ == '__main__':
    main()
