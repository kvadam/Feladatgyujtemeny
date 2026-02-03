def main() -> None:
    print("1. példa:")
    szam = 10.56
    print(f"{szam} -> {round(szam)}")
    print("2. példa:")
    print(round(1.0))
    print(round(1.49))
    print(round(1.5))
    print(round(2.5))
    print(round(2.51))
    print(round(3.5))
    print(round(4.5))
    print("3. példa:")
    print(round(10.465768, 4))

if __name__ == "__main__":
    main()
