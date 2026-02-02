def main() -> None:
    print("1. példa:")
    for i in range(5):
        print(i, end=" ")
    print("\n2. példa:")
    for i in range(1, 5):
        print(i, end=" ")
    print("\n3. példa:")
    for i in range(2, 11, 2):
        print(i, end=" ")
    print("\n4. példa:")
    for i in range(10, 0, -1):
        print(i, end=" ")
    print("\n5. példa:")
    for i in range(-5, 6, 1):
        print(i, end=" ")
    print("\n6. példa:")
    szamok = list(range(1, 11))
    print(szamok)


if __name__ == "__main__":
    main()
