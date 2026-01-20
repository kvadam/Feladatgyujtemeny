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
            rendelesek.append(Rendeles(int(s[0]), s[1], int(s[2])))


def feladat2() -> None:
    print("2. feladat:")
    print(f"A rendelések száma: {len(rendelesek)}")


def feladat3() -> None:
    print("3. feladat:")
    # nap: int = int(input("Kérem, adjon meg egy napot: "))
    nap: int = 9
    print(f"A rendelések száma az adott napon: {sum([1 for rendeles in rendelesek if rendeles.nap == nap])}")


def feladat4() -> None:
    print("4. feladat:")

    nr: set[int] = set()
    [nr.add(rendeles.nap) for rendeles in rendelesek if rendeles.varos == "NR"]

    print(f"{30 - len(nr)} nap nem volt a reklámban nem érintett városból rendelés") if (30 - len(nr)) > 0 else (
    print("Minden nap volt rendelés a reklámban nem érintett városból"))


def feladat5() -> None:
    print("5. feladat:")



def osszes(varos: str, nap: int) -> int:
    pass


def feladat7():
    print("7. feladat:")



def feladat8():
    print("8. feladat:")


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
