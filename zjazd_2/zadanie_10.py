napis = input("Podaj napis: ")
liczniki_liter = {}

# zliczyć
for litera in napis:
    if litera in liczniki_liter:
        liczniki_liter[litera] = liczniki_liter[litera] + 1
    else:
        liczniki_liter[litera] = 1

# wyświetlić
for litera in liczniki_liter:
    print(f"litera: {litera} wystąpiła {liczniki_liter[litera]} razy")
