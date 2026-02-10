from dataclasses import dataclass

@dataclass
class Auto:
    rendszam: str
    ajtok_szama: int
    hengerurtaltalom: float
    automata: bool

# Kezdd innen: ==========================================================================
x = 40500
y = 5.99
kod = "MT228"
bekapcsolt = False
paros = True
ossz = 50 + 22.50
cim = "Németi út" + " " + str(22) + "."
autok = ["Audi", "Mazda", "Renault"]
tipus = autok[0] + " A4"
rendelesek = [24, 19, 27, 31, 23]
kapcsolok = [False, False, True, False]
allapot = kapcsolok[1] | kapcsolok[2]
szorasok = [0.22, 0.56, 0.41]
ermek = {2020: 8, 2021: 9, 2022: 6, 2023: 9}
bev_lista = {"kenyér": 1, "tej": 2, "tojás": 10, "tészta": 1}
adatok = [[12, 14, 17], [10, 9, 13], [20, 20, 22], [16, 18, 19]]
e = ermek[2021] * adatok[2][0]
eladasok  = {"PL": [0, 0, 0], "TV": [0, 0, 0], "NR": [0, 0, 0]}
statisztika = [{"ev": 2023, "ma": {"ki": 28, "pld": 92000}, "kf": {"ki": 19, "pld": 54000}},
               {"ev": 2024, "ma": {"ki": 33, "pld": 110500}, "kf": {"ki": 18, "pld": 60000}},
               {"ev": 2025, "ma": {"ki": 34, "pld": 121000}, "kf": {"ki": 20, "pld": 61500}}]
kiad24ma = statisztika[1]["ma"]["ki"]
autoim = [Auto("JKL-123", 5, 1.1, False), Auto("AB CD-456", 5, 1.6, True)]
