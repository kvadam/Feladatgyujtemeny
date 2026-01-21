def main() -> None:
    # Változó deklarációja string típusú értékkel
    s = "alma"
    # Üres string létrehozása
    u = ""
    # String változó deklarációja a típus kiírásával
    s2: str = "alma"
    # A változó érték felülírható más típusú értékkel, de a 2. esetben figyelmeztetést kapunk.
    s = 5
    s2 = 5
    print(s, s2)
    # Kétféle string jelölés létezik
    s = "alma"
    s2 = 'fa'
    # Idézőjel használata string-en belül
    print('"Jó olvasó holtig olvas" Hegedűs Géza')
    # Két szöveg összefűzése
    s3 = s + s2
    print(s3)
    # Variáció összefűzésre
    s3 = s + " " + s2
    print(s3)
    # Nem ajánlott összefűzési módszer
    s3 = "alma" "fa"
    print(s3)

    s3 = "  Alma Körte  "
    # Szöveg feldarabolása szóköz karakter mentén (alapértelmezett működés)
    v1 = s3.split()
    print(v1)
    # Szöveg feldarabolása explicit módon kiírt szóköz karakter mentén
    v1 = s3.split(" ")
    print(v1)
    # Láthatatlan karakterek eltávolítása (szóköz, tabulátor, sortörés)
    v1 = s3.strip()
    print(v1)
    v1 = s3.upper()
    print(v1)

if __name__ == "__main__":
    main()
