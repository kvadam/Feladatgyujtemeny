from dataclasses import dataclass

@dataclass()
class Konyv:
    ev: int
    negyedev: int
    eredet: str
    adatok: str
    peldanyszam: int


@dataclass()
class Osszesito:
    ev: int
    magyarki: int
    magyarpld: int
    kulfoldiki: int
    kulfoldipld: int


konyvek: list[Konyv] = list()
statisztika: list[Osszesito] = list()

def feladat1() -> None:
    with open("../forras/kiadas.txt", "r", encoding='utf-8') as forras:
        for sor in forras:
            s = sor.strip().split(";")
            konyv: Konyv = Konyv(int(s[0]), int(s[1]), s[2], s[3], int(s[4]))
            konyvek.append(konyv)


def feladat2() -> None:
    print("2. feladat")
    # !!! szerzo = input("Szerző: ")
    szerzo = "Benedek Elek"
    db: int = 0
    for konyv in konyvek:
        if szerzo in konyv.adatok:
            db += 1

    if db > 0:
        print(f"{db} könyvkiadás")
    else:
        print("Nem adtak ki")


def feladat3() -> None:
    print("3. feladat")
    pld = 0
    alkalom = 0
    for konyv in konyvek:
        if pld < konyv.peldanyszam:
            pld = konyv.peldanyszam
            alkalom = 1
        elif pld == konyv.peldanyszam:
            alkalom += 1

    print(f"Legnagyobb példányszám: {pld}, előfordult {alkalom} alkalommal")


def feladat4() -> None:
    print("4. feladat")
    for konyv in konyvek:
        if konyv.eredet == "kf" and konyv.peldanyszam >= 40000:
            print(f"{konyv.ev}/{konyv.negyedev}. {konyv.adatok}")
            break


def feladat5() -> None:
    print("5. feladat")
    ev = 0
    i = -1
    for konyv in konyvek:
        if konyv.ev != ev:
            ev = konyv.ev
            statisztika.append(Osszesito(ev, 0, 0, 0, 0))
            i += 1

        if konyv.eredet == "ma":
            statisztika[i].magyarki += 1
            statisztika[i].magyarpld += konyv.peldanyszam
        else:
            statisztika[i].kulfoldiki += 1
            statisztika[i].kulfoldipld += konyv.peldanyszam

    print("Év\t\tMagyar kiadás\tMagyar példányszám\tKülföldi kiadás\tKülföldi példányszám")
    for ossz in statisztika:
        print(f"{ossz.ev}\t\t\t{ossz.magyarki}\t\t\t{ossz.magyarpld}\t\t\t{ossz.kulfoldiki}\t\t\t\t{ossz.kulfoldipld}")

    with open("tabla.html", "w", encoding='utf-8') as tabla:
        tabla.write("<table>\n")
        tabla.write(
            "<tr><th>Év</th><th>Magyar kiadás</th><th>Magyar példányszám</th><th>Külföldi kiadás</th><th>Külföldi példányszám</th></tr>\n")
        for ossz in statisztika:
            tabla.write(
                f"<tr><td>{ossz.ev}</td><td>{ossz.magyarki}</td><td>{ossz.magyarpld}</td><td>{ossz.kulfoldiki}</td><td>{ossz.kulfoldipld}</td></tr>\n")
        tabla.write("</table>\n")


def feladat6() -> None:
    print("6. feladat")
    print("Legalább kétszer, nagyobb példányszámban újra kiadott könyvek:")
    egyedi_kiadasok = set()

    for konyv in konyvek:
        egyedi_kiadasok.add(konyv.adatok)

    for egyedi_kiadas in egyedi_kiadasok:
        db: list[int] = list()
        for konyv in konyvek:
            if egyedi_kiadas == konyv.adatok:
                db.append(konyv.peldanyszam)

        elso_kiadas_db = db[0]
        hanyszor = 0
        for i in range(1, len(db)):
            if db[i] > elso_kiadas_db:
                hanyszor += 1

        if hanyszor >= 2:
            print(egyedi_kiadas)


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()


if __name__ == "__main__":
    main()
