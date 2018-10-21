LICZBA_DNI_TYGODNIA = 7

numer_dnia = 1
suma_temperatur = 0

min_ = None
max_ = None

while numer_dnia <= LICZBA_DNI_TYGODNIA:
    temp = int(input(f"Podaj temperaturę z dnia {numer_dnia}: "))
    suma_temperatur += temp

    if min_ is None or temp < min_:
        min_ = temp

    if max_ is None or temp > max_:
        max_ = temp

    numer_dnia += 1

srednia_temperatur = suma_temperatur / LICZBA_DNI_TYGODNIA

print(f'Srednia temperatura w tygodniu to {srednia_temperatur}')
print(f'Temperatura minimalna to było: {min_}')
print(f'Temperatura maksymalna to było: {max_}')
