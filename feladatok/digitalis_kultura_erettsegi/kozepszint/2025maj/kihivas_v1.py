print("1. feladat")
aktivitas: str = input("Adja meg az aktivitását: ")

print("2. feladat")
u: int = 0
g: int = 0
f: int = 0
k: int = 0
for a in aktivitas:
    if a == "U":
        u += 1
    elif a == "G":
        g += 1
    elif a == "F":
        f += 2
    elif a == "K":
        k += 10
elert_tav: int = u + g + f + k
print(f"Az elért távolság: {elert_tav}.")

print("3. feladat")
if u > 0 and g > 0 and f > 0 and k > 0:
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