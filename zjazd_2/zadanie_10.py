napis = input("Podaj napis: ")
liczniki_liter = {}

# zliczyć
for litera in napis:
    liczniki_liter[litera] = liczniki_liter.get(litera, 0) + 1

# wyświetlić
for litera in liczniki_liter:
    print(f"litera: {litera} wystąpiła {liczniki_liter[litera]} razy")
