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