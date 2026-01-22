import random

def main() -> None:
    szamok: list[int] = list(range(1, 11))
    print(f"Számsorozat: {szamok}")

    # random.seed(3867)

    print("1. példa")

    x = random.randint(5, 15)
    print(x)

    print("2. példa")
    # 0-1 között
    x = random.random()
    print(x)

    print("3. példa")
    # 50-100 között
    x = random.random() * 50 + 50
    print(x)

    print("4. példa")

    x = random.choice(szamok)
    print(x)

    print("5. példa")

    x = random.sample(szamok, 3)
    print(x)



if __name__ == '__main__':
    main()
