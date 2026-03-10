"""
Konstansok:
    n: Egész := 7
    t: Tömb[1..n] := {5, 8, 10, 5, 10, 8, 7}
Változók:
    e: Tömb[1..n]
    db: Egész := 0
    i, j: Egész
    van: Logikai
Program:
2)  Ciklus i := 1-től n-ig
1)      van := HAMIS
3)      Ciklus j := 1-től db-ig
5)          Ha t[i] = e[j] akkor
4)              van := IGAZ
6)              Kilépés a ciklusból
8)          Elágazás vége
7)      Ciklus vége
10)     Ha van = HAMIS akkor
9)          db := db + 1
11)         e[db] := t[i]
13)     Elágazás vége
12) Ciklus vége
14) Ki: e[1..db]
Program vége
"""

t: list[int] = [5, 8, 10, 5, 10, 8, 7]
e: list[int] = list()
van: bool

for i in range(len(t)):
    van = False
    for j in range(len(e)):
        if t[i] == e[j]:
            van = True
            break
    if not van:
        e.append(t[i])
print(e)


szamok = [2, 0, -5, 4]

i = 0
while i < len(szamok) and szamok[i] >= 0:
    i += 1

if i < len(szamok):
    print("Van negatív")
else:
    print("Nincs negatív")

i = 0
while i < len(szamok):
    if szamok[i] < 0:
        break
    i += 1

if i < len(szamok):
    print("Van negatív")
else:
    print("Nincs negatív")


szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

t = [szamok[i:i+4] for i in range(0,len(szamok), 4)]
print(t)

def vasarlas() -> tuple[int, int]:
    arak: list[int] = [200, 300, 400]
    kredit: int = int(input("Add meg mennyi kredited van: "))
    szallitasi_koltseg: int = 300

    osszar = 0
    for ar in arak:
        osszar += ar

    if osszar < 1000:
        print("A megrendelések értéke nem éri el az 1000 kreditet.")
        return kredit, 0
    if kredit < osszar + szallitasi_koltseg:
        print("Nincs elég kredit a vásárláshoz.")
        return kredit, 0
    if osszar > 5000:
        szallitasi_koltseg = 0

    husegpontok: int = osszar // 100
    kredit -= osszar + szallitasi_koltseg - husegpontok
    return kredit, husegpontok



eredmeny: tuple[int, int] = vasarlas()
print(eredmeny)