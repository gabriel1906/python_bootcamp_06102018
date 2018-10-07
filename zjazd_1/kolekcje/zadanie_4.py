# 1. stworzyć listę z liczbami od 0 do 100

lista = list(range(101))

# 2. utworzyć listę podzielnych przez 3 lub 5
wynik = []

# 3. przejść przez listę z 1. i pododawac do list z kroku 2.
for el in lista:
    if el % 3 == 0 or el % 5 == 0:
        wynik.append(el)

# 4. wypisać
print("Liczby podzielne przez 3 lub 5:")
print()
for el in wynik:
    print(el)
print()
print(f"W przedziale 0-100 jest {len(wynik)} liczb podzielnych przez 3 lub 5")

print("   ", end="")

x = range(1, 999, 75)

for i in x:
    print(f'{i:6}', end='')
print('cost')