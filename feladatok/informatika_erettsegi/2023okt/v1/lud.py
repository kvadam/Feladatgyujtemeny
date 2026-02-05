dobasok: list[int] = list()

def feladat1() -> None:
    global dobasok
    with open("dobasok.txt", "r", encoding="utf-8") as d:
        dobasok = list(map(lambda x: int(x), d.readline().strip().split()))
    print(dobasok)


def main() -> None:
    feladat1()


if __name__ == '__main__':
    main()
