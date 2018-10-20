def wiecej_niz(napis, prog):
    liczniki_liter = {}
    wynik = set()

    for litera in napis:
        litera = litera.lower()
        liczniki_liter[litera] = liczniki_liter.get(litera, 0) + 1
    for key, value in liczniki_liter.items():
        if value > prog:
           wynik.add(key)
    return wynik


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 0) == set()

def test_wiecej_niz_dla_niepustego_napisu_z_zbyt_wysokim_progiem():
    assert wiecej_niz("aaaaa", 10) == set()

def test_wiecej_niz_dla_niepusteg_napisu():
    assert wiecej_niz("aaaaabbbccd", 2) == {'a', 'b'}

def test_wiecej_niz_dla_niepustego_napisu_duze_male_litery():
    assert wiecej_niz("aaaAAbbbccd", 4) == {'a'}
