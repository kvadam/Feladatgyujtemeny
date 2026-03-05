from dataclasses import dataclass

@dataclass
class Meres:
    varos: str
    ora: int
    perc: int
    irany: str
    ero: int
    homerseklet: int


meresek: list[Meres] = list()

def feladat1() -> None:
    with open("../forras/tavirathu13.txt", "r", encoding="utf-8") as forras:
        for sor in forras:
            s = sor.strip().split()
            m = Meres(s[0], int(s[1][0:2]), int(s[1][2:4]), str(s[2][0:3]), int(s[2][3:5]), int(s[3]))
            meresek.append(m)


def feladat2() -> None:
    print("2. feladat")
    # varos: str = input("Adja meg egy település kódját! Település: ")
    varos: str = "BP"
    i: int = len(meresek) - 1
    while meresek[i].varos != varos:
        i -= 1
    print(f"Az utolsó mérési adat a megadott településről {meresek[i].ora}:{meresek[i].perc}-kor érkezett.")


def feladat3() -> None:
    print("3. feladat")
    minm: Meres = meresek[0]
    maxm: Meres = meresek[0]
    for i in range(len(meresek)):
        if meresek[i].homerseklet < minm.homerseklet:
            minm = meresek[i]
        if meresek[i].homerseklet > maxm.homerseklet:
            maxm = meresek[i]
    print(f"A legalacsonyabb hőmérséklet: {minm.varos} {minm.ora:02d}:{minm.perc:02d} {minm.homerseklet} fok.")
    print(f"A legmagasabb hőmérséklet: {maxm.varos} {maxm.ora:02d}:{maxm.perc:02d} {maxm.homerseklet} fok.")


def feladat4() -> None:
    print("4. feladat")
    volt_szelcsend = False
    for meres in meresek:
        if meres.irany == "000" and meres.ero == 0:
            print(f"{meres.varos} {meres.ora:02d}:{meres.perc:02d}")
            volt_szelcsend = True

    if not volt_szelcsend:
        print("Nem volt szélcsend a mérések idején.")


def feladat5() -> None:
    print("5. feladat")
    varosok: set[str] = set()
    for meres in meresek:
        varosok.add(meres.varos)
    for varos in varosok:
        idopontok: list[int] = [1, 7, 13, 19]
        osszeg: int = 0
        db: int = 0
        minh: int = 10000
        maxh: int = -10000
        for meres in meresek:
            if meres.varos == varos:
                if meres.ora in idopontok:
                    idopontok.remove(meres.ora)
                osszeg += meres.homerseklet
                db += 1
                if meres.homerseklet < minh:
                    minh = meres.homerseklet
                if meres.homerseklet > maxh:
                    maxh = meres.homerseklet
        # Itt a hőingadozás csak akkor megfelelő, ha a számok pozitívak, ellenkező esetben vizsgálat szükséges.
        print(f"{varos} Középhőmérséklet: {round(osszeg / db) if len(idopontok) == 0 else "NA"}; Hőmérséklet-ingadozás: {maxh - minh}")


def feladat6() -> None:
    print("6. feladat")
    varosok: set[str] = set()
    for meres in meresek:
        varosok.add(meres.varos)
    for varos in varosok:
        eleresi_ut = f"kimenet/{varos}.txt"
        with open(eleresi_ut, "w", encoding="utf-8") as fajl:
            fajl.write(f"{varos}\n")
            for meres in meresek:
                if meres.varos == varos:
                    fajl.write(f"{meres.ora:02d}:{meres.perc:02d} {"#" * meres.ero}\n")


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()


if __name__ == '__main__':
    main()