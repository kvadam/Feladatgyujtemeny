from dataclasses import dataclass

@dataclass
class Bejegyzes:
    nap: int
    ido: str
    rendszam: str
    sz_azon: str
    km_szam: int
    parkol: bool


bejegyzesek: list[Bejegyzes] = list()

def feladat1() -> None:
    with open("../forras/autok.txt", "r", encoding="utf-8") as forras:
        for sor in forras:
            s: list[str] = sor.strip().split(" ")
            nap: int = int(s[0])
            ido: str = s[1]
            rendszam: str = s[2]
            sz_azon: str = s[3]
            km_szam: int = int(s[4])
            parkol: bool = bool(int(s[5]))
            bejegyzesek.append(Bejegyzes(nap, ido, rendszam, sz_azon, km_szam, parkol))


def feladat2() -> None:
    print("2. feladat")
    utoljara_elvitt: Bejegyzes = bejegyzesek[0]
    for bejegyzes in reversed(bejegyzesek):
        if not bejegyzes.parkol:
            utoljara_elvitt = bejegyzes
            break
    print(f"{utoljara_elvitt.nap}. nap rendszám: {utoljara_elvitt.rendszam}")


def feladat3() -> None:
    print("3. feladat")
    # nap: int = int(input("Nap: "))
    nap: int = 4
    print(f"Forgalom a(z) {nap}.napon")
    for bejegyzes in bejegyzesek:
        if bejegyzes.nap == nap:
            if bejegyzes.parkol:
                print(f"{bejegyzes.ido} {bejegyzes.rendszam} {bejegyzes.sz_azon} be")
            else:
                print(f"{bejegyzes.ido} {bejegyzes.rendszam} {bejegyzes.sz_azon} ki")


def feladat4() -> None:
    print("4. feladat")
    autok: dict[str, bool] = {"CEG300": True, "CEG301": True, "CEG302": True, "CEG303": True, "CEG304": True,
                              "CEG305": True, "CEG306": True, "CEG307": True, "CEG308": True, "CEG309": True}
    for bejegyzes in bejegyzesek:
        autok[bejegyzes.rendszam] = bejegyzes.parkol
    kinn_van: int = 0
    for auto in autok.values():
        if not auto:
            kinn_van += 1
    print(f"A hónap végén {kinn_van} autót nem hoztak vissza.")


def feladat5() -> None:
    print("5. feladat")
    autok: dict[str, list[int]] = {"CEG300": [0, 0], "CEG301": [0, 0], "CEG302": [0, 0], "CEG303": [0, 0], "CEG304": [0, 0],
                                   "CEG305": [0, 0], "CEG306": [0, 0], "CEG307": [0, 0], "CEG308": [0, 0], "CEG309": [0, 0]}
    for bejegyzes in bejegyzesek:
        if autok[bejegyzes.rendszam][0] == 0:
            autok[bejegyzes.rendszam][0] = bejegyzes.km_szam
        autok[bejegyzes.rendszam][1] = bejegyzes.km_szam
    for rendszam, km in autok.items():
        print(f"{rendszam} {km[1] - km[0]} km")



def feladat6() -> None:
    print("6. feladat")
    autok: dict[str, list[int]] = {"CEG300": [0, 0], "CEG301": [0, 0], "CEG302": [0, 0], "CEG303": [0, 0],
                                   "CEG304": [0, 0],
                                   "CEG305": [0, 0], "CEG306": [0, 0], "CEG307": [0, 0], "CEG308": [0, 0],
                                   "CEG309": [0, 0]}
    leghosszabb_ut: int = 0
    szemely: str = ""
    for bejegyzes in bejegyzesek:
        if not bejegyzes.parkol and autok[bejegyzes.rendszam][0] == 0:
            autok[bejegyzes.rendszam][0] = bejegyzes.km_szam
        if bejegyzes.parkol and autok[bejegyzes.rendszam][1] == 0:
            autok[bejegyzes.rendszam][1] = bejegyzes.km_szam
            tav: int = autok[bejegyzes.rendszam][1] - autok[bejegyzes.rendszam][0]
            if tav > leghosszabb_ut:
                leghosszabb_ut = tav
                szemely = bejegyzes.sz_azon
            autok[bejegyzes.rendszam][0] = 0
            autok[bejegyzes.rendszam][1] = 0
    print(f"Leghosszabb út: {leghosszabb_ut} km, személy: {szemely}")


def feladat7() -> None:
    print("7. feladat")
    # rendszam: str = input("Rendszám: ")
    rendszam: str = "CEG304"
    menetlevel: list[Bejegyzes] = list()
    for bejegyzes in bejegyzesek:
        if bejegyzes.rendszam == rendszam:
            menetlevel.append(bejegyzes)
    eleresi_ut: str = f"{rendszam}_menetlevel.txt"
    with open(eleresi_ut, "w", encoding="utf-8") as menetlevel_txt:
        for bejegyzes in menetlevel:
            if not bejegyzes.parkol:
                menetlevel_txt.write(f"{bejegyzes.sz_azon}\t{bejegyzes.nap}.\t{bejegyzes.ido}\t{bejegyzes.km_szam} km")
            else:
                menetlevel_txt.write(f"\t{bejegyzes.nap}.\t{bejegyzes.ido}\t{bejegyzes.km_szam} km\n")
    print("Menetlevél kész.")


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()


if __name__ == "__main__":
    main()
