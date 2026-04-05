from dataclasses import dataclass

@dataclass
class Keppont:
    r: int
    g: int
    b: int


keppontok: list[list[Keppont]] = list()

def feladat1() -> None:
    with open("../forras/kep.txt", "r", encoding="utf-8") as forras:
        i: int = 0
        for sor in forras:
            s: list[int] = list(map(int, sor.strip().split(" ")))
            keppontok.append(list())
            for j in range(0, len(s), 3):
                keppontok[i].append(Keppont(s[j], s[j+1], s[j+2]))
            i += 1


def feladat2() -> None:
    print("2. feladat")
    print("Kérem egy képpont adatait!")
    # x: int = int(input("Sor: "))
    # y: int = int(input("Oszlop: "))
    x: int = 180
    y: int = 320
    print(f"A képpont színe RGB({keppontok[x-1][y-1].r}, {keppontok[x-1][y-1].g}, {keppontok[x-1][y-1].b})")


def feladat3() -> None:
    print("3. feladat")
    vilagos: int = sum(1 for sor in keppontok for keppont in sor if (keppont.r + keppont.g + keppont.b) > 600)
    print(f"A világos képpontok száma: {vilagos}")


def feladat4() -> None:
    print("4. feladat")
    min_ossz: int = min([kp.r + kp.g + kp.b for sor in keppontok for kp in sor])
    [print(f"RGB({kp.r}, {kp.g}, {kp.b})") for sor in keppontok for kp in sor if (kp.r + kp.g + kp.b) == min_ossz]


def hatar(ssz: int, elteres: int) -> bool:
    for i in range(1, len(keppontok[ssz-1])):
        if abs(keppontok[ssz-1][i-1].b - keppontok[ssz-1][i].b) > elteres:
            return True
    return False


def feladat6() -> None:
    legelso: int = -1
    legutolso: int = -1
    for i in range(len(keppontok)):
        if hatar(i, 10):
            if legelso < 0:
                legelso = i
            legutolso = i
    print(f"A felhő legfelső sora: {legelso}")
    print(f"A felhő legalsó sora: {legutolso}")


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat6()


if __name__ == '__main__':
    main()
