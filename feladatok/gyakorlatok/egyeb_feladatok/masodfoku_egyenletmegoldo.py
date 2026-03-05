import math

def main() -> None:
    a: int = int(input('Add meg az "a" együttható értékét: '))
    b: int = int(input('Add meg az "b" együttható értékét: '))
    c: int = int(input('Add meg az "c" együttható értékét: '))

    d: int = b * b - 4 * a * c

    if d > 0:
        x1: float = (-b + math.sqrt(d)) / (2 * a)
        x2: float = (-b - math.sqrt(d)) / (2 * a)
        print(f"Az egyenlet megoldásai: x1 = {x1}; x2 = {x2}")
    elif d == 0:
        x: float = (-b + math.sqrt(d)) / (2 * a)
        print(f"Az egyenlet megoldása: x = {x}")
    else:
        print("Az egyenletnek nincs megoldása.")



if __name__ == '__main__':
    main()
