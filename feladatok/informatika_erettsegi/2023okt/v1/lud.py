dobasok: list[int] = list()
osvenyek: list[str] = list()

def feladat1() -> None:
    global dobasok
    with open("../forras/dobasok.txt", "r", encoding="utf-8") as dobasok_txt:
        adatok = dobasok_txt.readline().strip().split()
        for adat in adatok:
            dobasok.append(int(adat))

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
    leghosszabb_i: int = 0
    for i in range(1, len(osvenyek)):
        if len(osvenyek[i]) > len(osvenyek[leghosszabb_i]):
            leghosszabb_i = i
    print(f"Az egyik leghosszabb a(z) {leghosszabb_i + 1}. ösvény, hossza: {len(osvenyek[leghosszabb_i])}")


def feladat4() -> tuple[int, int]:
    print("\n4. feladat")
    # osveny_ssz: int = int(input("Adja meg egy ösvény sorszámát! ")) - 1
    # jatekosok_szama: int = int(input("Adja meg a játékosok számát! "))
    osveny_ssz: int = 9-1
    jatekosok_szama: int = 5
    return osveny_ssz, jatekosok_szama


def feladat5(osveny_ssz: int) -> None:
    print("\n5. feladat")
    mezok: dict[str, int] = {}
    for mezo in osvenyek[osveny_ssz]:
        if mezo not in mezok:
            mezok[mezo] = 0
        mezok[mezo] += 1

    for mezo in mezok:
        print(f"{mezo}: {mezok[mezo]} darab")


def feladat6(osveny_ssz: int) -> None:
    with open("kulonleges.txt", "w", encoding="utf-8") as kulonleges_txt:
        osveny: str = osvenyek[osveny_ssz]
        for i in range(len(osveny)):
            if osveny[i] != "M":
                kulonleges_txt.write(f"{i + 1}\t{osveny[i]}\n")


def feladat7(osveny_ssz: int, jatekosok_szama: int) -> None:
    print("\n7. feladat")
    osveny: str = osvenyek[osveny_ssz]
    cel: int = len(osveny)
    jatekallas: list[int] = list()
    for _ in range(jatekosok_szama):
        jatekallas.append(0)
    korok_szama: int = 0
    dobas_i: int = 0

    while cel > max(jatekallas):
        korok_szama += 1
        for jatekos_i in range(len(jatekallas)):
            jatekallas[jatekos_i] += dobasok[dobas_i]
            dobas_i += 1

    print(f"A játék a(z) {korok_szama}. körben fejeződött be. A legtávolabb jutó(k) sorszáma:", end="")
    legnagyobb_tav: int = max(jatekallas)
    for jatekos_i in range(len(jatekallas)):
        if jatekallas[jatekos_i] == legnagyobb_tav:
             print(f" {jatekos_i + 1}", end="")
    print()


def feladat8(osveny_ssz: int, jatekosok_szama: int) -> None:
    print("\n8. feladat")
    osveny: str = osvenyek[osveny_ssz]
    cel: int = len(osveny)
    jatekallas: list[int] = list()
    for _ in range(jatekosok_szama):
        jatekallas.append(0)
    dobas_i: int = 0

    while cel > max(jatekallas):
        for jatekos_i in range(len(jatekallas)):
            jatekallas[jatekos_i] += dobasok[dobas_i]
            if jatekallas[jatekos_i] < cel:
                if osveny[jatekallas[jatekos_i] - 1] == "E":
                    jatekallas[jatekos_i] += dobasok[dobas_i]
                elif osveny[jatekallas[jatekos_i] - 1] == "V":
                    jatekallas[jatekos_i] -= dobasok[dobas_i]
            dobas_i += 1

    print(f"Nyertes(ek):", end="")
    for jatekos_i in range(len(jatekallas)):
        if jatekallas[jatekos_i] >= cel:
            print(f" {jatekos_i + 1}", end="")

    print("\nA többiek pozíciója:")
    for jatekos_i in range(len(jatekallas)):
        if jatekallas[jatekos_i] < cel:
            print(f"{jatekos_i + 1}. játékos, {jatekallas[jatekos_i]}. mező")


def main() -> None:
    feladat1()
    feladat2()
    feladat3()
    osveny_ssz, jatekosok_szama = feladat4()
    feladat5(osveny_ssz)
    feladat6(osveny_ssz)
    feladat7(osveny_ssz, jatekosok_szama)
    feladat8(osveny_ssz, jatekosok_szama)


if __name__ == '__main__':
    main()
