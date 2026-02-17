import math

"""Deklarálunk egy listát, melynek elemeit felsoroljuk.
 | Létrehozunk egy lista adatszerkezetet a kezdőértékek megadásával. """
szamok = [2, 6, 9, 5, 3]
# szamok = [9, 6, 2, 5, 3]
# szamok = [2, 6, 2, 5, 9]
# szamok = [2, 6, 7, 5, 3]

"""Feladat:
Döntsük el, hogy van-e a listában négyzetszám.

Szövegértelmezés:
1. "Döntsük el": Meg kell vizsgálni minden listaelemre, hogy tartalmaz-e a lista adott tulajdonságú elemet.
  - Minden elemet ki kell olvasni a listából és megvizsgálni, mert csak így garantálhatjuk a jó eredményt.
  - Viszont a vizsgálatot, csak az első találatig kell folytatni.
  - Az eredmény logikai. Igen/Nem választ várnak a kérdésre.
2.  "négyzetszám: az adott tulajdonságot fogja jelenteni, amit keresünk.
3.  "van-e": A vizsgálat kimenetele láthatóan egy logikai értéke lesz. (Vagy tartalmaz ilyet, vagy nem.)
    Továbbá a tulajdonság jelenlétét kell vizsgálni. (Akkor igaz ha van, különben hamis.)  
Ebből már látjuk, hogy az eldöntés tételét kell alkalmazni.
Az eldöntés tetele: 
    index := 0
    Ciklus amíg index < sokaság_elemszáma és NEM adott tulajdonságú sokaság[index]
        index := index + 1
    Ciklus vége
    Ha index < sokaság_elemszáma, akkor
       Ki: van adott tulajdonságú elem
    Különben
       Ki: nincs adott tulajdonságú elem
    Elágazás vége
A megoldás megtervezése:
  - Először átgondoljuk, hogy hogyan azonosíthatóak a négyzetszámok. Ha egy számból gyököt vonunk és  
    egészszámmá alakíthatjuk, majd kivonva belőle a gyök értékét és az eredmény nulla, akkor az négyzetszám. 
    Ehhez kell gyökvonás, egésszé alakítás és összehasonlítás.
  - Mivel ez sok számítás egy feltételben, ezért érdemes egy függvényt írni rá.
  - A gyökvonáshoz be kell importálni a matematikai csomagot: import math.
  - Tudjuk, hogy a gyökvonás math.sqrt() függvénnyel történik.
  - A számot az int() függvénnyel alakíthatjuk át egésszé.
  - Miután ezt megállapítottuk, utána választunk ciklust a feladat megoldásához. Azokban az esetekben, amikor 
    nem biztos, hogy minden elemet érinteni fogunk, lehet while ciklust használni.
"""

# 1. megoldás
def negyzetszam_e(x: int) -> bool:
    gyok: float = math.sqrt(float(x))
    return (int(gyok) - gyok) == 0


i: int = 0
while i < len(szamok) and not negyzetszam_e(szamok[i]):
    i += 1

if i < len(szamok):
    print("A számok közt van négyzetszám.")
else:
    print("A számok közt nincs négyzetszám.")


"""
Választhatjuk azt a módszert is a négyszetszám meghatározására, hogy elvégzünk egy isqrt műveletet, ami a 
megadott számból gyököt von, de egész végeredményt ad a tizedesek elhagyásával.
Ha az így kapott gyököket összeszorozzuk és az eredeti számot kapjuk vissza, akkor a szám négyzetszám volt.
"""

# 2. megoldást
def negyzetszam_e(x: int) -> bool:
    gyok: int = math.isqrt(x)
    return gyok * gyok == x


i: int = 0
while i < len(szamok) and not negyzetszam_e(szamok[i]):
    i += 1

if i < len(szamok):
    print("A számok közt van négyzetszám.")
else:
    print("A számok közt nincs négyzetszám.")