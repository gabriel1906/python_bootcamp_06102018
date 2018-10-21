def policz_znaki(napis, start="<", stop=">"):
    poziom_zaglebienia = 0
    wynik = 0
    for znak in napis:
        if znak == start:
            poziom_zaglebienia += 1
        elif znak == stop:
            poziom_zaglebienia -= 1
        else:
            wynik += poziom_zaglebienia
    return wynik


# # testy pomocnicze
#
# def test_0_poziom_zaglebienia():
#     assert policz_znaki("to jest napis") == 0
#
# def test_1_poziom_zaglebienia():
#     assert policz_znaki("to <jest napis") == 1
#
# def test_3_poziom_zaglebienia():
#     assert policz_znaki("to <jest <nap<is") == 3
#
# def test_2_poziom_zaglebienia():
#     assert policz_znaki("to <jest <nap<is>") == 2
#
# def test_2_poziom_zaglebienia():
#     assert policz_znaki("to [jest [nap[is]", '[', ']') == 2


def test_policz_znak_pusty_napis():
    assert policz_znaki('') == 0


def test_policz_znak_napis_bez_znacznikow():
    assert policz_znaki('to jest napis') == 0


def test_policz_znaki_jeden_level_wartosci_domyslne():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4


def test_policz_znaki_dwa_levele():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18


def test_policz_znaki_trzy_levele():
    assert policz_znaki('a <a<a<a>>>') == 6

