def main() -> None:
    s1 = ""
    s2 = "alma"
    s3 = "Alma Körte"
    s4 = "  \t Alma \n\tKörte  "
    s5 = " * Alma * Körte * "

    for x in list(locals().values()):
        print(f'"{x.strip()}"')

    print(f'"{s5.strip("*")}"')
    print(f'"{s5.strip(" *")}"')


if __name__ == "__main__":
    main()
