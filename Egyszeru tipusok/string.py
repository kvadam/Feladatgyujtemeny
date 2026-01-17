def main() -> None:
    # Változó deklarációja string típusú értékkel
    s = "alma"
    # String változó deklarációja a típus kiírásával
    s2: str = "alma"
    # A változó érték felülírható más típusú értékkel, de a 2. esetben figyelmeztetést kapunk.
    s = 5
    s2 = 5
    print(s2)
    # Kétféle string jelölés létezik
    s = "alma"
    s2 = 'fa'
    # Idézőjel használata string-en belül
    print('"Jó olvasó holtig olvas" Hegedűs Géza')
    # Két szöveg összefűzése
    s3 = s + s2
    print(s3)
    # Variáció összefűzésre
    s4 = s + " " + s2
    print(s4)
    # Nem ajánlott összefűzési módszer
    s5 = "alma" "fa"
    print(s5)


if __name__ == "__main__":
    main()
