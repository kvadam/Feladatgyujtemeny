tevekenysegek: dict[str, int] = {"U": 1, "G": 1, "F": 2, "K": 10}

print("1. feladat")
aktivitas: str = input("Adja meg az aktivitását: ")

print("2. feladat")
elert_tav: int = 0
for a in aktivitas:
    elert_tav += tevekenysegek[a]
print(f"Az elért távolság: {elert_tav}.")

print("3. feladat")
if len(set(aktivitas)) == 4:
    print("Bravó! a jutalma még 10 km.")
    elert_tav += 10
else:
    print("Nem jár jutatom.")

print("4. feladat")
print(f"Eredménye: {elert_tav} km. ", end="")
if elert_tav > 40:
    print("Gratulálok, kihívás teljesítve!")
else:
    print("Legközelebb sikerül!")