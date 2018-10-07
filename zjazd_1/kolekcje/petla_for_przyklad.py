lista = [1,2,3,4,5,6,1,2,3,4,5]

a, b, c = (1, 2, 3)

print(a)
print(b)
print(c)

for element in lista:
    pass

for licznik, zmienna_tymczasowa in enumerate(lista, 100):
    # zrob cos ze zmienna_tymczasowa
    print(licznik, zmienna_tymczasowa, zmienna_tymczasowa ** 2)


