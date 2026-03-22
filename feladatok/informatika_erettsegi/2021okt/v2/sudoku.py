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
            tablazat.append([int(szam) for szam in forras.readline().strip().split(" ")])
        for sor in forras:
            s: list[str] = sor.strip().split()
            lepesek.append(Lepes(int(s[0]), int(s[1]), int(s[2])))


def feladat3(sor: int, oszlop: int) -> None:
    print("3. feladat")
    if tablazat[sor-1][oszlop-1] == 0:
        print("Az adott helyet még nem töltötték ki.")
        return
    print(f"Az adott helyen szereplő szám: {tablazat[sor-1][oszlop-1]}")
    print(f"A hely a(z) {(sor // 3) * 3 + oszlop // 3 + 1} résztáblához tartozik.")


def feladat4() -> None:
    print("4. feladat")
    nullak_szama: int = sum(1 for sor in tablazat for szam in sor if szam == 0)
    print(f"Az üresek aránya: {((nullak_szama / 81) * 100):0.1f}%")


def feladat5() -> None:
    print("5. feladat")
    for l in lepesek:
        sor = l.sor - 1
        oszlop = l.oszlop - 1

        print(f"A kiválasztott sor: {l.sor} oszlop: {l.oszlop} a szám: {l.szam}")
        # Kitöltötték
        if tablazat[sor][oszlop] != 0:
            print("A helyet már kitöltöltötték.")
            continue
        # Sorban szerepel
        if l.szam in tablazat[sor]:
            print("Az adott sorban már szerepel a szám.")
            continue
        # Oszlopban szerepel
        if l.szam in [tablazat[i][oszlop] for i in range(9)]:
            print("Az adott oszlopban már szerepel a szám.")
            continue
        # Résztáblában szerepel
        resztablaban_van: bool = False
        for i in range(3 * (sor // 3), 3 * (sor // 3) + 3):
            for j in range(3 * (oszlop // 3), 3 * (oszlop // 3) + 3):
                if tablazat[i][j] == l.szam:
                    resztablaban_van = True
                    break
            if resztablaban_van:
                break
        if resztablaban_van:
            print("Az adott résztáblázatban már szerepel a szám.")
            continue
        # Lépés megtehető
        print("A lépés megtehető")


def main() -> None:
    print("1. feladat")
    # fajlnev: str = input("Adja meg a bemeneti fájl nevét! ")
    # sor: int = int(input("Adja meg egy sor számát! "))
    # oszlop: int = int(input("Adja meg a bemeneti fájl nevét! "))
    fajlnev: str = "konnyu.txt"
    sor: int = 1
    oszlop: int = 1
    feladat2(fajlnev)
    feladat3(sor, oszlop)
    feladat4()
    feladat5()


if __name__ == '__main__':
    main()
