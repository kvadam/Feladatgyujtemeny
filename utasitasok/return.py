def osszead1(x: int, y: int) -> int:
    osszeg = x + y
    return osszeg

def osszead2(x: int, y: int) -> int:
    return x + y

def main() -> None:
    print("1. példa:")
    print(osszead1(10, 20))
    print("2. példa:")
    print(osszead2(10, 20))


if __name__ == "__main__":
    main()
