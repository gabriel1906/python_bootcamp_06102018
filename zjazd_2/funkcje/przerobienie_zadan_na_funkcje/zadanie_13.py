def pobieranie_danych(ile_razy=7):
    temperatury = []
    for i in range(ile_razy):
        temp = int(input(f"Podaj temperaturę z dnia {i+1}: "))
        temperatury.append(temp)
    return temperatury


def srednia_temp(temperatury):
    return sum(temperatury) / len(temperatury)


def znajdz_ekstrma(temperatury):
    min_ = min(temperatury)
    max_ = max(temperatury)
    return min_, max_


def prezentuj_dane(srednia_temperatura, min_, max_):
    print(f'Srednia temperatura w tygodniu to {srednia_temperatura}')
    print(f'Temperatura minimalna to było: {min_}')
    print(f'Temperatura maksymalna to było: {max_}')


dane = pobieranie_danych()
sr_temp = srednia_temp(dane)
min_, max_ = znajdz_ekstrma(dane)
prezentuj_dane(sr_temp, min_, max_)
