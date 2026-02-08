dobasok: list[int]
osvenyek: list[str] = list()

with open("../forras/dobasok.txt", "r", encoding="utf-8") as dobasok_txt:
    dobasok = list(map(int, dobasok_txt.readline().strip().split()))
with open("../forras/osvenyek.txt", "r", encoding="utf-8") as osvenyek_txt:
    [osvenyek.append(sor.strip()) for sor in osvenyek_txt]

print("2. feladat")
print(f"A dobások száma: {len(dobasok)}\nA ösvények száma: {len(osvenyek)}")

print("\n3. feladat")
leghosszabb_i: int = osvenyek.index(max(osvenyek, key=len))
print(f"Az egyik leghosszabb a(z) {leghosszabb_i + 1}. ösvény, hossza: {len(osvenyek[leghosszabb_i])}")

print("\n4. feladat")
# osveny_ssz: int = int(input("Adja meg egy ösvény sorszámát! ")) - 1
# jatekosok_szama: int = int(input("Adja meg a játékosok számát! "))
osveny_ssz: int = 9-1
jatekosok_szama: int = 5
osveny: str = osvenyek[osveny_ssz]

print("\n5. feladat")
mezok: dict[str, int] = {mezo: osveny.count(mezo) for mezo in "MVE"}
[print(f"{mezo}: {mezok[mezo]} darab") for mezo in mezok]

with open("kulonleges.txt", "w", encoding="utf-8") as kulonleges_txt:
    [kulonleges_txt.write(f"{i + 1}\t{osveny[i]}\n") for i in range(len(osveny)) if osveny[i] != "M"]

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

print("\n\n8. feladat")
cel: int = len(osveny)
jatekallas: list[int] = [0 for _ in range(jatekosok_szama)]
dobas_i: int = 0
while cel > max(jatekallas):
    for jatekos_i in range(len(jatekallas)):
        jatekallas[jatekos_i] += dobasok[dobas_i]
        dobas_i += 1
        if jatekallas[jatekos_i] >= cel:
            continue
        s: int = 1 if osveny[jatekallas[jatekos_i]-1] == "E" else -1 if osveny[jatekallas[jatekos_i]-1] == "V" else 0
        jatekallas[jatekos_i] += dobasok[dobas_i - 1] * s
print(f"Nyertes(ek):", end="")
[print(f" {i + 1}", end="") for i in range(len(jatekallas)) if jatekallas[i] >= cel]
print("\nA többiek pozíciója:")
[print(f"{i + 1}. játékos, {jatekallas[i]}. mező") for i in range(len(jatekallas)) if jatekallas[i] < cel]
