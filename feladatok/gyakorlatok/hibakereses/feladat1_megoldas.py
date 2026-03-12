"""
A feladat 27 hibát tartalmaz, elhelyezkedésük ( <- hibák száma a sorban):

arak: list[str] = [200, 300, 'négyszáz', 500] <- 2
kredit: int = float(input("Add meg mennyi kredited van: ") <- 2
szallitasi_koltseg: int = 300.0 <- 1

osszar: int += 0 <- 1
for ar in range(arak): <- 1
    osszar -= arak <- 2

vegrehajthato = true <- 1

if osszarak > 1000 <- 3
    vegrehajthato == False <- 1
    print(A megrendelések értéke nem éri el az 1000 kreditet.) <- 1
if kredit < osszar * szallitasi_koltseg: <- 1
    print{"Nincs elég kredit a vásárláshoz."] <- 2
    vegrehajt = True <- 2
if vegrehajthato = True: <- 1
    if osszes > 5000: <- 1
        szallitasi_koltseg = -300 <- 1
    husegpontok: int = osszar / 100 <- 1
    kredit += osszar + szallitasi_koltseg - husegpontok <- 1
    husegpontok = kredit <- 1
    print("Fennmaradó kreditek: {kredit}, fennmaradó hűségpontok: {husegpontok}")  <- 1
"""

print("#"*3)

arak: list[int] = [200, 300, 400, 500]
kredit: int = int(input("Add meg mennyi kredited van: "))
szallitasi_koltseg: int = 300

osszar: int = 0
for ar in arak:
    osszar += ar

vegrehajthato = True

if osszar < 1000:
    vegrehajthato = False
    print("A megrendelések értéke nem éri el az 1000 kreditet.")
if kredit < osszar + szallitasi_koltseg:
    print("Nincs elég kredit a vásárláshoz.")
    vegrehajthato = False
if vegrehajthato:
    if osszar > 5000:
        szallitasi_koltseg = 0
    husegpontok: int = osszar // 100
    kredit -= osszar + szallitasi_koltseg - husegpontok
    husegpontok = 0
    print(f"Fennmaradó kreditek: {kredit}, fennmaradó hűségpontok: {husegpontok}")
