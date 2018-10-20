liczby = set()

while True:
    komenda = input("Wprowadź liczbę lub k by zakończyć: ")
    if komenda == 'k':
        break
    liczba = int(komenda)
    liczby.add(liczba)

print(len(liczby & set(range(2, 101, 2))))
