dobasok: list[int]
osvenyek: list[str] = list()

def feladat1() -> None:
    global dobasok
    with open("../forras/dobasok.txt", "r", encoding="utf-8") as dobasok_txt:
        dobasok = list(map(int, dobasok_txt.readline().strip().split()))

    global osvenyek
    with open("../forras/osvenyek.txt", "r", encoding="utf-8") as osvenyek_txt:
        for sor in osvenyek_txt:
            osvenyek.append(sor.strip())


def feladat2() -> None:
    print("2. feladat")
    print(f"A dobások száma: {len(dobasok)}")
    print(f"A ösvények száma: {len(osvenyek)}")


def feladat3() -> None:
    print("\n3. feladat")
    leghosszabb_i: int = osvenyek.index(max(osvenyek, key=len))
    print(f"Az egyik leghosszabb a(z) {leghosszabb_i + 1}. ösvény, hossza: {len(osvenyek[leghosszabb_i])}")


def feladat4() -> tuple[str, int]:
    print("\n4. feladat")
    # osveny_ssz: int = int(input("Adja meg egy ösvény sorszámát! ")) - 1
    # jatekosok_szama: int = int(input("Adja meg a játékosok számát! "))
    osveny_ssz: int = 9-1
    jatekosok_szama: int = 5
    return osvenyek[osveny_ssz], jatekosok_szama


def feladat5(osveny: str) -> None:
    print("\n5. feladat")
    mezok: dict[str, int] = {mezo: osveny.count(mezo) for mezo in "MVE"}
    [print(f"{mezo}: {mezok[mezo]} darab") for mezo in mezok]


def feladat6(osveny: str) -> None:
    with open("kulonleges.txt", "w", encoding="utf-8") as kulonleges_txt:
        [kulonleges_txt.write(f"{i + 1}\t{osveny[i]}\n") for i in range(len(osveny)) if osveny[i] != "M"]


def feladat7(osveny: str, jatekosok_szama: int) -> None:
    print("\n7. feladat")
    cel: int = len(osveny)
    jatekallas: list[int] = [0 for _ in range(jatekosok_szama)]
    korok_szama: int = 0
    dobas_i: int = 0

    while cel > max(jatekallas):
        jatekallas = [jatekallas[jatekos_i] + dobasok[dobas_i + jatekos_i] for jatekos_i in range(len(jatekallas))]
        dobas_i += jatekosok_szama
        korok_szama += 1

    print(f"A játék a(z) {korok_szama}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: ", end="")
    [print(f" {i + 1}", end="") for i in range(len(jatekallas)) if jatekallas[i] == max(jatekallas)]


def specialis_e(mezo: str) -> int:
    return 1 if mezo == "E" else -1 if mezo == "V" else 0


def kovetkezo_kor(jatekallas: list[int], osveny: str, cel: int, dobas_i) -> tuple[list[int], int]:
    for jatekos_i in range(len(jatekallas)):
        jatekallas[jatekos_i] += dobasok[dobas_i]
        dobas_i += 1
        if jatekallas[jatekos_i] >= cel:
            continue
        jatekallas[jatekos_i] += dobasok[dobas_i - 1] * specialis_e(osveny[jatekallas[jatekos_i] - 1])
    return jatekallas, dobas_i


def feladat8(osveny: str, jatekosok_szama: int) -> None:
    print("\n\n8. feladat")
    cel: int = len(osveny)
    jatekallas: list[int] = [0 for _ in range(jatekosok_szama)]
    dobas_i: int = 0

    while cel > max(jatekallas):
        jatekallas, dobas_i = kovetkezo_kor(jatekallas, osveny, cel, dobas_i)

    print(f"Nyertes(ek):", end="")
    [print(f" {i + 1}", end="") for i in range(len(jatekallas)) if jatekallas[i] >= cel]
    print("\nA többiek pozíciója:")
    [print(f"{i + 1}. játékos, {jatekallas[i]}. mező") for i in range(len(jatekallas)) if jatekallas[i] < cel]


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    osveny, jatekosok_szama = feladat4()
    feladat5(osveny)
    feladat6(osveny)
    feladat7(osveny, jatekosok_szama)
    feladat8(osveny, jatekosok_szama)


if __name__ == '__main__':
    main()
