urtaltalmak: list[int] = [5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3]

print("2. feladat")
L: int = int(input("Mari néni lekvárja (dl): "))

print("3. feladat")
legnagyobb_i: int = 0
for i in range(len(urtaltalmak)):
    if urtaltalmak[i] > urtaltalmak[legnagyobb_i]:
        legnagyobb_i = i

print(f"A legnagyobb üveg: {urtaltalmak[legnagyobb_i]} dl és {legnagyobb_i + 1}. a sorban")

print("4. feladat")
print("Elegendő üveg volt.") if sum(urtaltalmak) >= L else print("Maradt lekvár.")
