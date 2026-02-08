from random import randint

aktualis_emelet: int = randint(0, 10)
cel_emelet: int = randint(0, 10)
haladas_iranya: str = "F" if cel_emelet > aktualis_emelet else "L" if cel_emelet < aktualis_emelet else "-"
print(f"A lift helyzete: {aktualis_emelet} {haladas_iranya} ({cel_emelet})")
hivo_szintje: int = int(input("Adja meg a szintet, ahonnan hívja a liftet! Szint: "))
if (hivo_szintje > aktualis_emelet >= cel_emelet) or (hivo_szintje < aktualis_emelet <= cel_emelet):
    print(f"A liftnek {abs(aktualis_emelet + hivo_szintje - 2 * cel_emelet)} emeletet kell haladnia a hívóig.")
else:
    print(f"A liftnek {abs(aktualis_emelet - hivo_szintje)} emeletet kell haladnia a hívóig.")