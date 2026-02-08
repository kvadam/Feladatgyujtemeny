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
    [print(f" {jeladas.ora}:{jeladas.perc}", end="") for jeladas in jeladasok if jeladas.rendszam == elso]
    print()


def feladat4() -> None:
    print("4. feladat")
    # ora: int = int(input("Kérem, adja meg az órát: "))
    # perc: int = int(input("Kérem, adja meg a percet: "))
    ora: int = 6
    perc: int = 54
    print(f"A jeladások száma: {sum([1 for jeladas in jeladasok if jeladas.ora == ora and jeladas.perc == perc])}")


def feladat5() -> None:
    print("5. feladat")
    legnagyobb_sebesseg: int = 0
    leggyorsabbak: list[str] = list()
    for jeladas in jeladasok:
        if jeladas.sebesseg > legnagyobb_sebesseg:
            legnagyobb_sebesseg = jeladas.sebesseg
            leggyorsabbak = [jeladas.rendszam]
        elif jeladas.sebesseg == legnagyobb_sebesseg:
            leggyorsabbak.append(jeladas.rendszam)

    print(f"A legnagyobb sebesség km/h: {legnagyobb_sebesseg}")
    print("A járművek:", end="")
    [print(f" {auto}", end="") for auto in leggyorsabbak]
    print()


def feladat6() -> None:
    print("6. feladat:")
    # rendszam: str = input("Kérem, adja meg a rendszámot: ")
    rendszam = "ZVJ-638"
    auto: list[Jeladas] = list()
    [auto.append(jeladas) for jeladas in jeladasok if jeladas.rendszam == rendszam]

    megtett_ut = 0.0
    print(f"{auto[0].ora}:{auto[0].perc} {megtett_ut:.1f} km")
    for i in range(1, len(auto)):
        k = kulonbseg(auto[i-1].ora, auto[i-1].perc, auto[i].ora, auto[i].perc)
        megtett_ut += auto[i-1].sebesseg * (k / 60)
        print(f"{auto[i].ora}:{auto[i].perc} {megtett_ut:.1f} km")


def feladat7() -> None:
    rendszamok: set[str] = {jeladas.rendszam for jeladas in jeladasok}

    with open("ido.txt", "w", encoding="utf-8") as ido_txt:
        for rendszam in rendszamok:
            ido: dict[str, int] = {"elso_ora": 0, "elso_perc": 0, "utolso_ora": 0, "utolso_perc": 0}
            for j in jeladasok:
                if rendszam == j.rendszam:
                    ido["elso_ora"] = j.ora
                    ido["elso_perc"] = j.perc
                    break
            for j in reversed(jeladasok):
                if rendszam == j.rendszam:
                    ido["utolso_ora"] = j.ora
                    ido["utolso_perc"] = j.perc
                    break
            ido_txt.write(f"{rendszam} {ido["elso_ora"]} {ido["elso_perc"]} {ido["utolso_ora"]} {ido["utolso_perc"]}\n")


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
