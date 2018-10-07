znalezione_max = None
znalezione_min = None


while True:
    dane_wejsciowe = input("Podaj liczbę, lub wpisz KONIEC by zakończyć: ")

    if dane_wejsciowe.lower() == "koniec":
        break

    liczba = int(dane_wejsciowe)
    if znalezione_max is None or liczba > znalezione_max:
        znalezione_max = liczba
    if znalezione_min is None or liczba < znalezione_min:
        znalezione_min = liczba

if not znalezione_max:
    print("Nie wprowadzono danych")
else:
    print(f"Minimum = {znalezione_min}, maximum = {znalezione_max}")

