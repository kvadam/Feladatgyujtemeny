def main() -> None:
    szoveg = "Ez egy példa mondat."
    print(szoveg)
    print(f"A szöveg hossza {len(szoveg)} karakter (0-{len(szoveg)-1}).")
    print(1, szoveg[:0])
    print(2, szoveg[:1])
    print(3, szoveg[:6])
    print(4, szoveg[0:])
    print(5, szoveg[1:])
    print(6, szoveg[7:])
    print(7, szoveg[:-1])
    print(8, szoveg[:-7])
    print(9, szoveg[-1:])
    print(10, szoveg[-7:])
    print(11, szoveg[0:0:1])
    print(12, szoveg[0:1:1])
    print(13, szoveg[0:2:1])
    print(14, szoveg[0:6:1])
    print(15, szoveg[7:12:1])
    print(16, szoveg[13:20:1])
    print(17, szoveg[0:20:3])
    print(18, szoveg[19:12:-1])
    print(19, szoveg[11:6:-1])
    print(20, szoveg[::-1])


if __name__ == '__main__':
    main()
