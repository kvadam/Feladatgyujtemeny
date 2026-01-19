from dataclasses import dataclass
from datetime import datetime, date, time, timedelta

@dataclass
class Esemeny:
    tanulo_azon: str
    idopont: time
    esemeny_azon: int

    def esemeny_kiiras(self) -> None:
        print(f"{self.tanulo_azon} {self.idopont:%H:%M} {self.esemeny_azon}")


adatok: list[Esemeny] = list()

def feladat1() -> None:
    with open("../forras/bedat.txt", "r", encoding="utf-8") as forras:
        for sor in forras:
            s: list[str] = sor.strip().split(" ")
            adat: Esemeny = Esemeny(s[0], time(int(s[1][:2]), int(s[1][3:]), 0), int(s[2]))
            adatok.append(adat)
            # adat.esemeny_kiiras()


def feladat2() -> None:
    print("2. feladat")
    for esemeny in adatok:
        if esemeny.esemeny_azon == 1:
            print(f"Az első tanuló {esemeny.idopont:%H:%M}-kor érkezett.")
            break

    for esemeny in reversed(adatok):
        if esemeny.esemeny_azon == 2:
            print(f"Az utolsó tanuló {esemeny.idopont:%H:%M}-kor távozott.")
            break


def feladat3() -> None:
    with open("kesok.txt", "w", encoding="utf-8") as kesok:
        for esemeny in adatok:
            if esemeny.idopont >= time(8,15):
                break
            if esemeny.idopont > time(7, 50) and esemeny.esemeny_azon == 1:
                kesok.write(f"{esemeny.idopont:%H:%M} {esemeny.tanulo_azon}\n")


def feladat4() -> int:
    print("4. feladat")
    ebedelt_fo: int = 0
    for esemeny in adatok:
        if esemeny.esemeny_azon == 3:
            ebedelt_fo += 1
    print(f"Ebédelt {ebedelt_fo} fő.")
    return ebedelt_fo


def feladat5(ebedelt_fo: int) -> None:
    print("5. feladat")
    kolcsonzok: list[str] = list()
    for esemeny in adatok:
        if esemeny.esemeny_azon == 4 and esemeny.tanulo_azon not in kolcsonzok:
            kolcsonzok.append(esemeny.tanulo_azon)

    print(f"A mai napon kölcsönzött {len(kolcsonzok)} fő")

    if ebedelt_fo > len(kolcsonzok):
        print("Többen ebédeltek.")
    else:
        print("Többen kölcsönöztek.")


def feladat6() -> None:
    print("6. feladat")
    v: list[Esemeny] = list()

    for esemeny in adatok:
        if esemeny.idopont > time(11, 00):
            break
        if esemeny.idopont > time(10, 50) and esemeny.esemeny_azon == 1:
            v.append(esemeny)

    for esemeny in v:
        benn_van: bool = False
        for adat in adatok:
            if esemeny.tanulo_azon != adat.tanulo_azon:
                continue

            if adat.esemeny_azon == 1 and benn_van and time(10, 50) < adat.idopont < time(11, 00):
                print(adat.tanulo_azon, end=" ")
            elif adat.esemeny_azon == 1:
                benn_van = True
            elif adat.esemeny_azon == 2:
                benn_van = False
    print()

def feladat7() -> None:
    print("7. feladat")
    tanulo_azon: str = input("Adj meg egy azonosítót: ")

    kezdo_ido: datetime = datetime(1, 1, 1, 0, 0)
    veg_ido: datetime = datetime(1, 1, 1, 0, 0)
    for esemeny in adatok:
        if esemeny.tanulo_azon != tanulo_azon:
            continue
        kezdo_ido = datetime.combine(kezdo_ido, esemeny.idopont)
        break

    if kezdo_ido == datetime(1, 1, 1, 0, 0):
        print("Nem volt iskolában.")
        return

    for esemeny in reversed(adatok):
        if esemeny.tanulo_azon != tanulo_azon:
            continue
        veg_ido = datetime.combine(veg_ido, esemeny.idopont)
        break

    temp: float = (veg_ido - kezdo_ido).total_seconds()
    ora: int = int(temp // 3600) # 7320 // 3600 = 2
    perc: int = int(temp % 3600 // 60)  # 7300 % 3600 -> 120 // 60 = 2
    print(f"{ora} óra {perc} perc")


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
