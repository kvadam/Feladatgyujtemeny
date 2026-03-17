from dataclasses import dataclass

@dataclass
class Lepes:
    szam: int
    sor: int
    oszlop: int


tablazat: list[list[int]] = list()
lepesek: list[Lepes] = list()


def feladat2(fajlnev: str) -> None:
    eleresi_ut: str = "../forras/" + fajlnev
    with open(eleresi_ut, "r", encoding="utf-8") as forras:
        for i in range(0, 9):
            tablazat.append(list(map(int, forras.readline().strip().split(" "))))

        for sor in forras:
            s: list[str] = sor.strip().split()
            lepesek.append(Lepes(int(s[0]), int(s[1]), int(s[2])))


def feladat3(sor: int, oszlop: int) -> None:
    print("3. feladat")
    print(f"Az adott helyen szereplő szám: {tablazat[sor-1][oszlop-1]}")
    a: int = (sor // 3) * 3
    b: int = oszlop // 3
    print(f"A hely a(z) {a + b + 1} résztáblához tartozik.")


def feladat4() -> None:
    nullak_szama: int = 0
    for sor in tablazat:
        for szam in sor:
            if szam == 0:
                nullak_szama += 1
    print(f"Az üresek aránya: {((nullak_szama / 81) * 100):0.1f}%")


def feladat5() -> None:
    for l in lepesek:
        print(f"A kiválasztott sor: {l.sor} oszlop: {l.oszlop} a szám: {l.szam}")
        # Kitöltötték
        if tablazat[l.sor-1][l.oszlop-1] != 0:
            print("A helyet már kitöltöltötték.")
            continue
        # Sorban szerepel
        if l.szam in tablazat[l.sor-1]:
            print("Az adott sorban már szerepel a szám.")
            continue
        # Oszlopban szerepel
        i: int = 0
        while i < 9 and tablazat[i][l.oszlop-1]:
            i += 1
        if i < 9:
            continue
        # Résztáblában szerepel
        a: int = (l.sor // 3) * 3
        b: int = l.oszlop // 3


def main() -> None:
    print("1. feladat")
    # fajlnev: str = input("Adja meg a bemeneti fájl nevét! ")
    fajlnev: str = "konnyu.txt"
    # sor: int = int(input("Adja meg egy sor számát! "))
    sor: int = 1
    # oszlop: int = int(input("Adja meg a bemeneti fájl nevét! "))
    oszlop: int = 1
    feladat2(fajlnev)
    feladat3(sor, oszlop)
    feladat4()
    feladat5()


if __name__ == '__main__':
    main()
