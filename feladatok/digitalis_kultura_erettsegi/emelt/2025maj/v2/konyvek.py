from dataclasses import dataclass
from functools import reduce

@dataclass()
class Konyv:
    ev: int
    negyedev: int
    eredet: str
    adatok: str
    peldanyszam: int


konyvek: list[Konyv] = list()

def feladat1() -> None:
    with open("../forras/kiadas.txt", "r", encoding='utf-8') as forras:
        adatok = [sor.strip().split(";") for sor in forras]
        [konyvek.append(Konyv(int(s[0]), int(s[1]), s[2], s[3], int(s[4]))) for s in adatok]


def feladat2() -> None:
    print("2. feladat")
    # !!! szerzo = input("Szerző: ")
    szerzo = "Benedek Elek"
    db: int = sum([1 for konyv in konyvek if szerzo in konyv.adatok])
    print(f"{db} könyvkiadás") if db > 0 else print("Nem adtak ki")


def feladat3() -> None:
    print("3. feladat")
    legnagyobb_peldanyszam: int = reduce(lambda x, y: x if x.peldanyszam > y.peldanyszam else y, konyvek).peldanyszam
    alkalom: int = sum([1 for konyv in konyvek if konyv.peldanyszam == legnagyobb_peldanyszam])
    print(f"Legnagyobb példányszám: {legnagyobb_peldanyszam}, előfordult {alkalom} alkalommal")


def feladat4() -> None:
    print("4. feladat")
    i: int = 0
    while konyvek[i].eredet != "kf" or konyvek[i].peldanyszam < 40000:
        i += 1
    print(f"{konyvek[i].ev}/{konyvek[i].negyedev}. {konyvek[i].adatok}")


def feladat5() -> None:
    print("5. feladat")
    aktualis_ev = 0
    i = -1
    statisztika: list[dict[str, int | dict[str, int]]] = list()
    for konyv in konyvek:
        if konyv.ev != aktualis_ev:
            aktualis_ev = konyv.ev
            statisztika.append({"ev": aktualis_ev, "ma": {"ki": 0, "pld": 0}, "kf": {"ki": 0, "pld": 0}})
            i += 1

        statisztika[i][konyv.eredet]["ki"] += 1
        statisztika[i][konyv.eredet]["pld"] += konyv.peldanyszam

    with open("tabla.html", "w", encoding='utf-8') as tabla:
        print("Év\t\tMagyar kiadás\tMagyar példányszám\tKülföldi kiadás\tKülföldi példányszám")
        tabla.write("<table>\n")
        tabla.write(
            "<tr><th>Év</th><th>Magyar kiadás</th><th>Magyar példányszám</th><th>Külföldi kiadás</th><th>Külföldi példányszám</th></tr>\n")

        for ev in statisztika:
            print(f"{ev["ev"]}\t\t\t{ev["ma"]["ki"]}\t\t\t{ev["ma"]["pld"]}\t\t\t{ev["kf"]["ki"]}\t\t\t\t{ev["kf"]["pld"]}")
            tabla.write(f"<tr><td>{ev["ev"]}</td><td>{ev["ma"]["ki"]}</td><td>{ev["ma"]["pld"]}</td><td>{ev["kf"]["ki"]}</td><td>{ev["kf"]["pld"]}</td></tr>\n")

        tabla.write("</table>\n")


def feladat6() -> None:
    print("6. feladat")
    print("Legalább kétszer, nagyobb példányszámban újra kiadott könyvek:")
    egyedi_kiadasok: set[str] = set([konyv.adatok for konyv in konyvek])

    for egyedi_kiadas in egyedi_kiadasok:
        db: list[int] = [konyv.peldanyszam for konyv in konyvek if egyedi_kiadas == konyv.adatok]
        hanyszor_nagyobb = sum([1 for i in range(1, len(db)) if db[i] > db[0]])
        if hanyszor_nagyobb >= 2: print(egyedi_kiadas)


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()


if __name__ == "__main__":
    main()
