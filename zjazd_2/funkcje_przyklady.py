

def przywitaj_sie(imie, wiek, wzrost, waga):
    print("Witaj ", imie)
    if wzrost > 178:
        print("Ale z Ciebie drągal")
    if waga > 100:
        print("Boczek")
    if wiek > 38:
        print("To takie staruchy jeszcze żyja")

lista_osob = [
    {
        'imie': "Rafał",
        'wiek': 38,
        'wzrost': 181,
        'waga': 102,
    },
    {
        'imie': "Adam",
        'wiek': 40,
        'wzrost': 178,
        'waga': 80,
    },
    {
        'imie': "Agnieszka",
        'wiek': 25,
        'wzrost': 188,
        'waga': 76,
    },
]



for osoba in lista_osob:
    przywitaj_sie(osoba['imie'], osoba['wiek'], osoba['wzrost'], osoba['waga'])


def czy_wieksza_niz_3(liczba):
    if liczba > 3:
        return True
    # return False
    return False

def test_czy_wieksza_niz_3_dla_wiekszej_niz_3():
    assert czy_wieksza_niz_3(4)

def test_czy_wieksza_niz_3_dla_mniejszej_niz_3():
    assert czy_wieksza_niz_3(2) == False
