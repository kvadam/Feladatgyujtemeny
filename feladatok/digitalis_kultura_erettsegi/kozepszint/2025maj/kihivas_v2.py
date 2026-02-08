tevekenysegek: dict[str, int] = {"U": 1, "G": 1, "F": 2, "K": 10}

print("1. feladat")
aktivitas: str = input("Adja meg az aktivitását: ")

print("2. feladat")
elert_tav: int = sum([tevekenysegek[a] for a in aktivitas])
print(f"Az elért távolság: {elert_tav}.")

print("3. feladat")
negy_aktivitas: bool = len(set(aktivitas)) == 4
print("Bravó! a jutalma még 10 km.") if negy_aktivitas else print("Nem jár jutatom.")
if negy_aktivitas: elert_tav += 10

print("4. feladat")
print(f"Eredménye: {elert_tav} km. ", end="")
print("Gratulálok, kihívás teljesítve!") if elert_tav > 40 else print("Legközelebb sikerül!")
