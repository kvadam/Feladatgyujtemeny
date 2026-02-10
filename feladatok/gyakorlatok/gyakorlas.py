szamok = [2, 0, -5, 4]

i = 0
while i < len(szamok) and szamok[i] >= 0:
    i += 1

if i < len(szamok):
    print("Van negatív")
else:
    print("Nincs negatív")

i = 0
while i < len(szamok):
    if szamok[i] < 0:
        break
    i += 1

if i < len(szamok):
    print("Van negatív")
else:
    print("Nincs negatív")