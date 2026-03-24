from dataclasses import dataclass
from datetime import datetime

@dataclass
class Felszallo:
    mid: int
    fdat: str
    fid: str
    berlet: str
    edat: str


felszallok: list[Felszallo] = list()

def napokszama(e1: int, h1: int, n1: int, e2: int, h2: int, n2: int) -> int:
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1= 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2= 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) // 10 + n2 - 1
    return d2-d1



def feladat1() -> None:
    with open("../forras/utasadat.txt", "r", encoding="utf-8") as forras:
        for sor in forras:
            s: list[str] = sor.strip().split(" ")
            felszallok.append(Felszallo(int(s[0]), s[1], s[2], s[3], s[4]))


def feladat2() -> None:
    print("2. feladat")
    print(f"A buszra {len(felszallok)} utas akart felszállni.")


def feladat3() -> None:
    print("3. feladat")
    nem_utazhat: int = 0
    for f in felszallok:
        if f.edat == "0":
            nem_utazhat += 1
        # if napokszama(f.fdat[0::4], f.fdat[4::6], f.fdat[6::8], f.edat[0::4], f.edat[4::6], f.edat[6::8])
    print(f"A buszra ??? utas nem szállhatott fel.")


def main() -> None:
    feladat1()
    feladat2()
    feladat3()


if __name__ == '__main__':
    main()
