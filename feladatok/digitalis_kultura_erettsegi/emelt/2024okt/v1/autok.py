from dataclasses import dataclass

@dataclass
class Jeladas:
    rendszam: str
    ora: int
    perc: int
    sebesseg: int


jeladasok: list[Jeladas] = list()

def kulonbseg(ora1: int, perc1: int, ora2: int, perc2: int) -> int:
    return ((ora2 - ora1) * 60) + (perc2 - perc1)


def feladat1() -> None:
    with open("../forras/jeladas.txt", "r", encoding="utf-8") as forras:
        for sor in forras:
            s: list[str] = sor.strip().split("\t")
            jeladas = Jeladas(s[0], int(s[1]), int(s[2]), int(s[3]))
            jeladasok.append(jeladas)


def feladat2() -> None:
    print("2. feladat:")
    print(f"Az utolsó jeladás időpontja {jeladasok[-1].ora}:{jeladasok[-1].perc}, a jármű rendszáma {jeladasok[-1].rendszam}")


def feladat3() -> None:
    print("3. feladat:")
    elso: str = jeladasok[0].rendszam
    print(f"Az első jármű: {elso}")
    print("Jeladásainak időpontjai:", end="")
    for jeladas in jeladasok:
        if jeladas.rendszam == elso:
            print(f" {jeladas.ora}:{jeladas.perc}", end="")
    print()


def feladat4() -> None:
    print("4. feladat")
    # ora = int(input("Kérem, adja meg az órát: "))
    # perc = int(input("Kérem, adja meg a percet: "))
    ora = 6
    perc = 54
    db = 0
    for jeladas in jeladasok:
        if jeladas.ora == ora and jeladas.perc == perc:
            db += 1
    print(f"A jeladások száma: {db}")


def feladat5() -> None:
    print("5. feladat")
    legnagyobb_sebesseg = 0
    leggyorsabbak = list()
    for jeladas in jeladasok:
        if jeladas.sebesseg > legnagyobb_sebesseg:
            legnagyobb_sebesseg = jeladas.sebesseg
            list.clear(leggyorsabbak)
            leggyorsabbak.append(jeladas.rendszam)
        elif jeladas.sebesseg == legnagyobb_sebesseg:
            leggyorsabbak.append(jeladas.rendszam)

    print(f"A legnagyobb sebesség km/h: {legnagyobb_sebesseg}")
    print("A járművek:", end="")
    for auto in leggyorsabbak:
        print(f" {auto}", end="")
    print()


def feladat6() -> None:
    print("6. feladat:")
    # rendszam: str = input("Kérem, adja meg a rendszámot: ")
    rendszam = "ZVJ-638"
    auto: list[Jeladas] = list()
    for jeladas in jeladasok:
        if jeladas.rendszam == rendszam:
            auto.append(jeladas)

    # for j in auto:
    #     print(f"{j.rendszam} {j.ora} {j.perc} {j.sebesseg}")

    megtett_ut = 0.0
    print(f"{auto[0].ora}:{auto[0].perc} {megtett_ut:.1f} km")
    for i in range(1, len(auto)):
        k = kulonbseg(auto[i-1].ora, auto[i-1].perc, auto[i].ora, auto[i].perc)
        megtett_ut += auto[i-1].sebesseg * (k / 60)
        print(f"{auto[i].ora}:{auto[i].perc} {megtett_ut:.1f} km")


def feladat7() -> None:
    rendszamok: set[str] = set()
    for jeladas in jeladasok:
        rendszamok.add(jeladas.rendszam)

    with open("ido.txt", "w", encoding="utf-8") as ido:
        for rendszam in rendszamok:
            elso_ora: int = 0
            elso_perc: int = 0
            utolso_ora: int = 0
            utolso_perc: int = 0
            for j in jeladasok:
                if rendszam == j.rendszam:
                    elso_ora = j.ora
                    elso_perc = j.perc
                    break
            for j in reversed(jeladasok):
                if rendszam == j.rendszam:
                    utolso_ora = j.ora
                    utolso_perc = j.perc
                    break
            ido.write(f"{rendszam} {elso_ora} {elso_perc} {utolso_ora} {utolso_perc}\n")


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()


if __name__ == "__main__":
    main()
