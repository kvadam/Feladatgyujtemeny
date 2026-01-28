def main() -> None:
    szamok: list[int] = list(range(1, 11))
    print(f"Számsorozat: {szamok}")

    print("1. példa")

    legnagyobb: int = max(szamok)
    print(legnagyobb)


if __name__ == '__main__':
    main()
