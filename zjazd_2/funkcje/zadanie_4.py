"""
ver.1
Funkcja przyjmuje zmienna cena
oraz nieokreśloną liczbę tekstów.
W tych tekstach trzeba zamienić $cena na wartość zmiennej cena
Zwróć złączony tekst - kazdy tekst w nowej linii


"""


def formatuj(a, b, *args, marker='*', **kwargs):
    print(a*b)
    out = []
    for text in args:
        for k in kwargs:
            text = text.replace(f'{marker}{k}', str(kwargs[k]))
        out.append(text)
    return "\n".join(out)


def test_formatuj():
    assert formatuj(1, 2,
        'koszt cena PLN',
        'kwota cena brutto',
         cena = 10,
    ) == "koszt cena PLN\nkwota cena brutto"

    assert formatuj(1,2,
        'koszt *cena PLN',
        'kwota *cena brutto',
         cena = 10,
    ) == "koszt 10 PLN\nkwota 10 brutto"

    assert formatuj(1,2,
        'koszt *cena PLN',
        'kwota *cena brutto',
        'sumarycznie *cena',
        'podatek: *podatek',
        cena = 10,
        podatek = 0.23
    ) == "koszt 10 PLN\nkwota 10 brutto\nsumarycznie 10\npodatek: 0.23"


    assert formatuj(1,2,
        'koszt $cena PLN',
        'kwota $cena brutto',
        'sumarycznie $cena',
        'podatek: $podatek',
        marker="$",
        cena = 10,
        podatek = 0.23
    ) == "koszt 10 PLN\nkwota 10 brutto\nsumarycznie 10\npodatek: 0.23"
