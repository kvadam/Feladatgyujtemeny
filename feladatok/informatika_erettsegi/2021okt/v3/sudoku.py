from dataclasses import dataclass

@dataclass
class Lepes:
    szam: int
    sor: int
    oszlop: int


tablazat: list[list[int]] = list()
lepesek: list[Lepes] = list()

print("1. feladat")
# fajlnev: str = input("Adja meg a bemeneti fájl nevét! ")
# sor: int = int(input("Adja meg egy sor számát! "))
# oszlop: int = int(input("Adja meg a bemeneti fájl nevét! "))
fajlnev: str = "konnyu.txt"
sor: int = 1
oszlop: int = 1

# 2. feladat
eleresi_ut: str = "../forras/" + fajlnev
with open(eleresi_ut, "r", encoding="utf-8") as forras:
    for i in range(0, 9):
        tablazat.append([int(szam) for szam in forras.readline().strip().split(" ")])
    for be_sor in forras:
        s: list[str] = be_sor.strip().split()
        lepesek.append(Lepes(int(s[0]), int(s[1]), int(s[2])))


print("3. feladat")
if tablazat[sor-1][oszlop-1] == 0:
    print("Az adott helyet még nem töltötték ki.")
else:
    print(f"Az adott helyen szereplő szám: {tablazat[sor-1][oszlop-1]}")
    print(f"A hely a(z) {(sor // 3) * 3 + oszlop // 3 + 1} résztáblához tartozik.")

print("4. feladat")
nullak_szama: int = sum(1 for t_sor in tablazat for szam in t_sor if szam == 0)
print(f"Az üresek aránya: {((nullak_szama / 81) * 100):0.1f}%")

print("5. feladat")
for l in lepesek:
    print(f"A kiválasztott sor: {l.sor} oszlop: {l.oszlop} a szám: {l.szam}")
    sor_i: int = l.sor - 1
    oszlop_i: int = l.oszlop - 1
    # Kitöltötték
    if tablazat[sor_i][oszlop_i] != 0:
        print("A helyet már kitöltöltötték.\n")
        continue
    # Sorban szerepel
    if l.szam in tablazat[sor_i]:
        print("Az adott sorban már szerepel a szám.\n")
        continue
    # Oszlopban szerepel
    if l.szam in [tablazat[i][oszlop_i] for i in range(9)]:
        print("Az adott oszlopban már szerepel a szám.\n")
        continue
    # Résztáblában szerepel
    resztablaban_van: bool = False
    for i in range(3 * (sor_i // 3), 3 * (sor_i // 3) + 3):
        for j in range(3 * (oszlop_i // 3), 3 * (oszlop_i // 3) + 3):
            if tablazat[i][j] == l.szam:
                resztablaban_van = True
                break
        if resztablaban_van:
            break
    if resztablaban_van:
        print("Az adott résztáblázatban már szerepel a szám.\n")
        continue
    # Lépés megtehető
    print("A lépés megtehető.\n")
