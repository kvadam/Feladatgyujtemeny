from dataclasses import dataclass
from datetime import datetime, date, time, timedelta

@dataclass
class Esemeny:
    tanulo_azon: str
    idopont: time
    esemeny_azon: int


adatok: list[Esemeny] = list()

def feladat1() -> None:
    with open("../forras/bedat.txt", "r", encoding="utf-8") as forras:
        for sor in forras:
            s: list[str] = sor.strip().split(" ")
            adatok.append(Esemeny(s[0], time(int(s[1][:2]), int(s[1][3:]), 0), int(s[2])))


def feladat2() -> None:
    print("2. feladat")
    print(f"Az első tanuló {adatok[0].idopont:%H:%M}-kor érkezett.")
    print(f"Az utolsó tanuló {adatok[-1].idopont:%H:%M}-kor távozott.")


def feladat3() -> None:
    with open("kesok.txt", "w", encoding="utf-8") as kesok:
        for esemeny in adatok:
            if esemeny.idopont > time(8,15):
                break
            if esemeny.idopont > time(7, 50) and esemeny.esemeny_azon == 1:
                kesok.write(f"{esemeny.idopont:%H:%M} {esemeny.tanulo_azon}\n")


def feladat4() -> int:
    print("4. feladat")
    ebedelt_fo: int = sum([1 for esemeny in adatok if esemeny.esemeny_azon == 3])
    print(f"Ebédelt {ebedelt_fo} fő.")
    return ebedelt_fo


def feladat5(ebedelt_fo: int) -> None:
    print("5. feladat")
    kolcsonzok: set[str] = set([esemeny.tanulo_azon for esemeny in adatok if esemeny.esemeny_azon == 4])
    print(f"A mai napon kölcsönzött {len(kolcsonzok)} fő")

    print("Többen ebédeltek.") if ebedelt_fo > len(kolcsonzok) else print("Többen kölcsönöztek.")


def engedely_nelkuli_kilepes(esemeny: Esemeny) -> bool:
    benn_van: bool = False
    for adat in adatok:
        if esemeny.tanulo_azon != adat.tanulo_azon:
            continue

        if adat.esemeny_azon == 1 and benn_van and time(10, 50) < adat.idopont < time(11, 00):
            return True
        elif adat.esemeny_azon == 1:
            benn_van = True
        elif adat.esemeny_azon == 2:
            benn_van = False
    return False


def feladat6() -> None:
    print("6. feladat")
    kilepok: list[Esemeny] = [a for a in adatok if a.idopont > time(10, 50) and
                              a.idopont < time(11, 00) and a.esemeny_azon == 1]

    [print(esemeny.tanulo_azon, end=" ") for esemeny in kilepok if engedely_nelkuli_kilepes(esemeny)]
    print()

def feladat7() -> None:
    print("7. feladat")

    # tanulo_azon: str = input("Adj meg egy azonosítót: ")
    tanulo_azon: str = "ZOOM"
    idopontok = [esemeny.idopont for esemeny in adatok if esemeny.tanulo_azon == tanulo_azon]

    if len(idopontok) == 0:
        print("Nem volt iskolában.")
        return

    kezdo_ido = datetime.combine(datetime(1, 1, 1, 0, 0), idopontok[0])
    veg_ido = datetime.combine(datetime(1, 1, 1, 0, 0), idopontok[-1])
    ido: float = (veg_ido - kezdo_ido).total_seconds()
    print(f"A tanuló érkezése és távozása között {int(ido // 3600)} óra {int(ido % 3600 // 60)} perc telt el.")


def main():
    feladat1()
    feladat2()
    feladat3()
    ebedelt_fo = feladat4()
    feladat5(ebedelt_fo)
    feladat6()
    feladat7()


if __name__ == '__main__':
    main()
