from pathlib import Path

def keres(utvonal: Path, parancs: str) -> None:
    for objektum in utvonal.iterdir():

        if objektum.is_dir():
            keres(objektum, parancs)

        if objektum.name[-2:] == "py":
            with open(objektum, "r", encoding="utf-8") as forras:
                ssz = 1
                for sor in forras:
                    sor = sor.strip()
                    if parancs in sor:
                        print(f'File "{objektum}", line {ssz}')
                        print(f"\t{sor}\n")
                    ssz+=1


def main() -> None:
    projekt_mappa = Path(__file__).resolve().parent.parent
    feladatok_mappa = projekt_mappa / "feladatok"

    parancsnev: str = input("Milyen parancsot keresel?: ")
    keres(feladatok_mappa, parancsnev)


if __name__ == "__main__":
    main()
