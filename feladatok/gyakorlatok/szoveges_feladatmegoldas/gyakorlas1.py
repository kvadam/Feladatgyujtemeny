"""Deklarálunk egy listát, melynek elemeit felsoroljuk.
 | Létrehozunk egy lista adatszerkezetet a kezdőértékek megadásával. """
szamok = [-2, 0, 8, -5, 3]

"""Feladat:
Döntsük el, hogy van-e a listában négyzetszám.
Szövegértelmezés:
1. "Döntsük el": Meg kell vizsgálni minden listaelemre, hogy tartalmaz-e a lista adott tulajdonságú elemet.
  - Minden elemet ki kell olvasni a listából és megvizsgálni, mert csak így garantálhatjuk a jó eredményt.
  - Viszont a vizsgálatot, csak az első találatig kell folytatni.
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
    az eredmény egészszámmá alakítható, akkor az négyzetszám. Ehhez kell gyökvonás, egésszé alakítás és összehasonlítás
  - A gyökvonáshoz be kell importálni a matematikai csomagot: import math
  - Tudjuk, hogy a gyökvonás math.sqrt() függvénnyel történik
  - A számot az int() függvénnyel alakíthatjuk át
  - Miután ezt megállapítottuk, utána választunk ciklus a feladat megoldásához. Mi
"""

