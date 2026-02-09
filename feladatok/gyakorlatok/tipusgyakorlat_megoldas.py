from dataclasses import dataclass

@dataclass
class Auto:
    rendszam: str
    ajtok_szama: int
    hengerurtaltalom: float
    automata: bool

# Kezdd innen: ==========================================================================
x: int = 40500
y: float = 5.99
kod: str = "MT228"
bekapcsolt: bool = False
paros: bool = True
ossz: float = 50 + 22.50
cim: str = "Németi út" + " " + str(22) + "."
autok: list[str] = ["Audi", "Mazda", "Renault"]
tipus: str = autok[0] + " A4"
rendelesek: list[int] = [24, 19, 27, 31, 23]
kapcsolok: list[bool] = [False, False, True, False]
allapot: bool = kapcsolok[1] | kapcsolok[2]
szorasok: list[float] = [0.22, 0.56, 0.41]
ermek: dict[int, int] = {2020: 8, 2021: 9, 2022: 6, 2023: 9}
bev_lista: dict[str, int] = {"kenyér": 1, "tej": 2, "tojás": 10, "tészta": 1}
adatok: list[list[int]] = [[12, 14, 17], [10, 9, 13], [20, 20, 22], [16, 18, 19]]
e: int = ermek[2021] * adatok[2][0]
eladasok: dict[str, list[int]]  = {"PL": [0, 0, 0], "TV": [0, 0, 0], "NR": [0, 0, 0]}
statisztika: list[dict[str, int | dict[str, int]]] = [
            {"ev": 2023, "ma": {"ki": 28, "pld": 92000}, "kf": {"ki": 19, "pld": 54000}},
            {"ev": 2024, "ma": {"ki": 33, "pld": 110500}, "kf": {"ki": 18, "pld": 60000}},
            {"ev": 2025, "ma": {"ki": 34, "pld": 121000}, "kf": {"ki": 20, "pld": 61500}}]
ma24:dict[str, int] = statisztika[1]["ma"]
autoim: list[Auto] = [Auto("JKL-123", 5, 1.1, False), Auto("AB CD-456", 5, 1.6, True)]