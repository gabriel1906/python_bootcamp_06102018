def naleznosc(waga, cena_za_kg):
    return waga * cena_za_kg

def drukuj(waga, cena_za_kg):
    out = f"""Cena za kg: {cena_za_kg}
Waga: {waga}
Należność: {naleznosc(waga, cena_za_kg)}
"""
    return out, waga, cena_za_kg

def test_naleznosc():
    assert naleznosc(10, 10) == 100
    assert naleznosc(0, 1) == 0

def test_drukuj():
    out, waga, cena_za_kg = drukuj(20, 2.5)
    # wynik = drukuj(20, 25) # ( "  ....", 20, 2.5)
    # out = wynik[0]
    # waga = wynik[1]
    # ...
    assert out == """Cena za kg: 2.5
Waga: 20
Należność: 50.0
"""
