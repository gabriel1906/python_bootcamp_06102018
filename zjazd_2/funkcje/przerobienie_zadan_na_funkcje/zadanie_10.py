

def pobranie_danych():
    liczba_1 = int(input("Podaj liczbę pierwszą: "))
    liczba_2 = int(input("Podaj liczbę drugą: "))
    operacja = input("Rodzaj operacji: ")
    return liczba_1, liczba_2, operacja

def kalkulator(liczba_1, liczba_2, operacja):
    wynik = "nieustalony wynik"

    if operacja == "+":
        wynik = liczba_1 + liczba_2
    elif operacja == "-":
        wynik = liczba_1 - liczba_2
    elif operacja == "/":
        if liczba_2 == 0:
            raise ValueError("Liczba druga powinna być dla tej operacji różna od 0")
        wynik = liczba_1 / liczba_2
    elif operacja == "*":
        wynik = liczba_1 * liczba_2
    else:
        print("Wybrałes niezrozumiałą operację")
        # raise ValueError("Nieprawidłowa wartość dla parametry typ operacji")

    print("Wynik operacji: ", wynik)

def prezentuj_wynik():
    dane = pobranie_danych()
    try:
        wynik = kalkulator(*dane)
    except ValueError:
        wynik = "Operacja niedozwolona"
    print(wynik)

prezentuj_wynik()
