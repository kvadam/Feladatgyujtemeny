def main() -> None:
    eleresi_ut: str = "../feladatok/digitalis_kultura_erettsegi/emelt/2024maj/v1/belepteto.py"
    parancsnev: str = "print"
    with open(eleresi_ut, "r", encoding="utf-8") as forras:
        ssz = 1
        for sor in forras:
            if parancsnev in sor.strip():
                print(f'File "{eleresi_ut}", line {ssz}')
            ssz+=1

if __name__ == "__main__":
    main()
