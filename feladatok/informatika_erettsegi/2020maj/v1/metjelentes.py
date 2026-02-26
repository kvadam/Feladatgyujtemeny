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
            print(m)
            meresek.append(m)


def feladat2() -> None:
    print("2. feladat")
    varos = input("Adja meg egy település kódját! Település: ")
    for meres in reversed(meresek):
        if varos == meres.varos:
            print("")


def main() -> None:
    feladat1()


if __name__ == '__main__':
    main()