from dataclasses import dataclass
from datetime import time
import math

@dataclass
class Jel:
    ido: time
    x: int
    y: int


jeladasok: list[Jel] = list()

def feladat1() -> None:
    with open("../forras/jel.txt", "r", encoding="utf-8") as forras:
        for sor in forras:
            s: list[str] = sor.strip().split(" ")
            ido: time = time(int(s[0]), int(s[1]), int(s[2]))
            jeladasok.append(Jel(ido, int(s[3]), int(s[4])))


def feladat2() -> None:
    print("2. feladat")
    # ssz: int = int(input("Adja meg a jel sorszámát! "))
    ssz: int = 3
    print(f"x={jeladasok[ssz-1].x} y={jeladasok[ssz-1].y}")


def eltelt(kezd: time, veg: time) -> int:
    kezd_mp = kezd.hour * 3600 + kezd.minute * 60 + kezd.second
    veg_mp = veg.hour * 3600 + veg.minute * 60 + veg.second
    return veg_mp - kezd_mp


def feladat4() -> None:
    print("4. feladat")
    eltelt_mp: int = eltelt(jeladasok[0].ido, jeladasok[-1].ido)
    ora: int = eltelt_mp // 3600
    perc: int = (eltelt_mp % 3600) // 60
    mp: int = eltelt_mp % 60
    print(f"Időtartam: {ora}:{perc}:{mp}")


def feladat5() -> None:
    print("5. feladat")
    min_x: int = jeladasok[0].x
    min_y: int = jeladasok[0].y
    max_x: int = jeladasok[0].x
    max_y: int = jeladasok[0].y
    for i in range(1, len(jeladasok)):
        if jeladasok[i].x < min_x:
            min_x = jeladasok[i].x
        if jeladasok[i].y < min_y:
            min_y = jeladasok[i].y
        if jeladasok[i].x > max_x:
            max_x = jeladasok[i].x
        if jeladasok[i].y > max_y:
            max_y = jeladasok[i].y
    print(f"Bal alsó: {min_x} {min_y}, jobb felső: {max_x} {max_y}")


def feladat6() -> None:
    print("6. feladat")
    elmozdulas: int = 0
    for i in range(1, len(jeladasok)):
        elmozdulas += math.sqrt(pow((jeladasok[i].x - jeladasok[i-1].x), 2) + pow((jeladasok[i].y - jeladasok[i-1].y), 2))
    print(f"Elmozdulás: {elmozdulas:0.3f} egység")


def feladat7() -> None:
    with open("kimaradt.txt", "w", encoding="utf-8") as kimaradt:
        for i in range(1, len(jeladasok)):
            ido_kul: int = eltelt(jeladasok[i-1].ido, jeladasok[i].ido)
            kimaradt_tav: int = 0
            kimaradt_ido: int = 0
            if ido_kul > 300:
                kimaradt_ido = (ido_kul - 1) // 300
            tav: int = max(abs(jeladasok[i-1].x - jeladasok[i].x), abs(jeladasok[i-1].y - jeladasok[i].y))
            if tav > 10.0:
                kimaradt_tav = (tav - 1) // 10
            if kimaradt_tav > kimaradt_ido:
                ido: time = jeladasok[i].ido
                kimaradt.write(f"{ido.hour} {ido.minute} {ido.second} koordináta-eltérés {kimaradt_tav}\n")
            if kimaradt_tav < kimaradt_ido:
                ido: time = jeladasok[i].ido
                kimaradt.write(f"{ido.hour} {ido.minute} {ido.second} időeltérés {kimaradt_ido}\n")



def main() -> None:
    feladat1()
    feladat2()
    feladat4()
    feladat5()
    feladat6()
    feladat7()


if __name__ == '__main__':
    main()
