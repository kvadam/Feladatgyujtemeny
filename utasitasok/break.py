def main() -> None:
    print("A ciklus előtti utasítás")

    for i in range(1, 11):
        if i > 3:
            break
        print(f"A ciklusmag lefutott ennyiszer: {i}")


    print("A ciklus utáni utasítás")


if __name__ == '__main__':
    main()
