dobasok: list[int] = list()
osvenyek: list[str] = list()

def feladat1() -> None:
    global dobasok
    with open("dobasok.txt", "r", encoding="utf-8") as dobasok_txt:
        dobasok = list(map(int, dobasok_txt.readline().strip().split()))

    global osvenyek
    with open("osvenyek.txt", "r", encoding="utf-8") as osvenyek_txt:
        for sor in osvenyek_txt:
            osvenyek.append(sor.strip())


def feladat2() -> None:
    print("2. feladat")
    print(f"A dobások száma: {len(dobasok)}")
    print(f"A ösvények száma: {len(osvenyek)}")


def feladat3() -> None:
    print("\n3. feladat")
    leghosszabb_i: int = 0
    for i in range(len(osvenyek)):
        if len(osvenyek[i]) > len(osvenyek[leghosszabb_i]):
            leghosszabb_i = i
    print(f"Az egyik leghosszabb a(z) {leghosszabb_i + 1}. ösvény, hossza: {len(osvenyek[leghosszabb_i])}")


def feladat4() -> list[int]:
    print("\n4. feladat")
    # osveny_ssz: int = int(input("Adja meg egy ösvény sorszámát! ")) - 1
    # jatekosok_szama: int = int(input("Adja meg a játékosok számát! "))
    osveny_ssz: int = 1-1
    jatekosok_szama: int = 5
    return [osveny_ssz, jatekosok_szama]


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
        osveny = osvenyek[osveny_ssz]
        for i in range(len(osveny)):
            if osveny[i] != "M":
                kulonleges_txt.write(f"{i + 1}\t{osveny[i]}\n")


def feladat7(osveny_ssz: int, jatekosok_szama: int) -> None:
    print("\n7. feladat")
    osveny: str = osvenyek[osveny_ssz]
    cel: int = len(osveny)
    jatekallas: list[int] = [0 for _ in range(jatekosok_szama)]
    korok_szama: int = 0
    dobas_i = 0

    while cel > max(jatekallas):
        korok_szama += 1
        for jatekos_i in range(len(jatekallas)):
            jatekallas[jatekos_i] += dobasok[dobas_i]
            dobas_i += 1

    print(f"A játék a(z) {korok_szama}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: ", end="")
    legnagyobb_tav: int = max(jatekallas)
    for jatekos_i in range(len(jatekallas)):
        if jatekallas[jatekos_i] == legnagyobb_tav:
             print(f"{jatekos_i + 1}")



def feladat8(osveny_ssz: int, jatekosok_szama: int) -> None:
    print("\n8. feladat")
    osveny: str = osvenyek[osveny_ssz]
    cel: int = len(osveny)
    jatekallas: list[int] = [0 for _ in range(jatekosok_szama)]
    dobas_i = 0

    while cel > max(jatekallas):
        for jatekos_i in range(len(jatekallas)):
            jatekallas[jatekos_i] += dobasok[dobas_i]
            if jatekallas[jatekos_i] > cel:
                dobas_i += 1
                continue
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
    adatok = feladat4()
    osveny_ssz: int = adatok[0]
    jatekosok_szama: int = adatok[1]
    feladat5(osveny_ssz)
    feladat6(osveny_ssz)
    feladat7(osveny_ssz, jatekosok_szama)
    feladat8(osveny_ssz, jatekosok_szama)


if __name__ == '__main__':
    main()
