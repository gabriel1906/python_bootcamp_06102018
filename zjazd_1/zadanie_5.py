
miasto_a = input("Podaj nazwę miasta A: ")
miasto_b = input("Podaj nazwę miasta B: ")
dystans = int(input(f"Podaj dystans między {miasto_a}-{miasto_b}: "))
cena_paliwa = float(input("Jaka jest cena paliwa: "))
spalanie = float(input("Okreś spalanie na 100km: "))

koszt = int((dystans / 100) * spalanie * cena_paliwa)

output = f'''
Miasto A: {miasto_a}
Miasto B: {miasto_b}
Dystans {miasto_a}-{miasto_b}: {dystans}
Cena paliwa: {cena_paliwa}
Spalanie na 100: {spalanie}

Koszt przejazdu {miasto_a}-{miasto_b} to {koszt} PLN
'''

print(output)