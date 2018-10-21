
def prezentuj_osobe(imie, wzrost):
    wynik = f"""Opis faceta:
    Imię: {imie}
    Wzrost: {wzrost}
"""
    return wynik


def test_prezentuj_osobe():
    assert prezentuj_osobe("Rafał", 181) == """Opis faceta:
    Imię: Rafał
    Wzrost: 181
"""
