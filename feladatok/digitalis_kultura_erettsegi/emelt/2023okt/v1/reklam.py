from dataclasses import dataclass

@dataclass
class Rendeles:
    nap: int
    varos: str
    db: int


rendelesek: list[Rendeles] = list()

def feladat1() -> None:
    with open("../forras/rendel.txt", "r", encoding="utf-8") as forras:
        for sor in forras:
            s: list[str] = sor.strip().split(" ")
            rendeles: Rendeles = Rendeles(int(s[0]), s[1], int(s[2]))
            rendelesek.append(rendeles)


def feladat2() -> None:
    print("2. feladat:")
    print(f"A rendelések száma: {len(rendelesek)}")


def feladat3() -> None:
    print("3. feladat:")
    # nap: int = int(input("Kérem, adjon meg egy napot: "))
    nap: int = 9
    rendelesek_szama: int = 0
    for rendeles in rendelesek:
        if rendeles.nap == nap:
            rendelesek_szama += 1
    print(f"A rendelések száma az adott napon: {rendelesek_szama}")


def feladat4() -> None:
    print("4. feladat:")
    volt_rendeles: int = 0
    aktualis_nap: int = 0
    for rendeles in rendelesek:
        if rendeles.nap != aktualis_nap and rendeles.varos == "NR":
            volt_rendeles += 1
            aktualis_nap = rendeles.nap

    if (30 - volt_rendeles) > 0:
        print(f"{30 - volt_rendeles} nap nem volt a reklámban nem érintett városból rendelés")
    else:
        print("Minden nap volt rendelés a reklámban nem érintett városból")


def feladat5() -> None:
    print("5. feladat:")
    legnagyobb_index: int = 0
    for i in range(len(rendelesek)):
        if rendelesek[i].db > rendelesek[legnagyobb_index].db:
            legnagyobb_index = i
    print(f"A legnagyobb darabszám: {rendelesek[legnagyobb_index].db}, a rendelés napja: {rendelesek[legnagyobb_index].nap}")


def osszes(varos: str, nap: int) -> int:
    osszes_db: int = 0
    for rendeles in rendelesek:
        if rendeles.varos == varos and rendeles.nap == nap:
            osszes_db += rendeles.db
    return osszes_db


def feladat7():
    print("7. feladat:")
    pl = osszes("PL", 21)
    tv = osszes("TV", 21)
    nr = osszes("NR", 21)
    print(f"A rendelt termékek darabszáma a 21. napon PL: {pl} TV: {tv} NR: {nr}")


def feladat8():
    print("8. feladat:")

    with open("kampany.txt", "w", encoding="utf-8") as kampany:
        print("Napok\t1..10\t11..20\t21..30")
        kampany.write("Napok\t1..10\t11..20\t21..30\n")

        eladasok: dict[str, list[int]]  = {"PL": [0, 0, 0], "TV": [0, 0, 0], "NR": [0, 0, 0]}

        for rendeles in rendelesek:
            i: int = (rendeles.nap - 1) // 10
            eladasok[rendeles.varos][i] += 1

        for varos in eladasok:
            print(varos, end="")
            kampany.write(varos)
            for eladas in eladasok[varos]:
                print(f"\t\t{eladas}", end="")
                kampany.write(f"\t\t{eladas}")
            print()
            kampany.write("\n")


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat7()
    feladat8()


if __name__ == "__main__":
    main()
