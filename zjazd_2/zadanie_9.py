produkty = {"ziemniaki": 2, "bataty": 4, "pomidory": 6}
magazyn = {"ziemniaki": 10, "bataty": 10, "pomidory": 10}
koszyk = {}
do_zaplaty = 0

while True:
    print("-"*40)
    print("Nasz zielnik oferuje: ")
    for produkt in produkty:
        print(f' - {produkt} - {produkty[produkt]} PLN')
    print()
    komenda = input("Co chcesz zrobić: [d]odać, [k]upić, [koniec] by zakończyć: ")
    if komenda == 'koniec':
        break
    elif komenda == 'k':
        produkt_wybrany = input("Co chcesz kupić? ")
        if produkt_wybrany not in produkty:
            print("Nie mamy takiego produktu!")
            continue

        waga = float(input(f"Ile chcesz kupić wybranego produktu [{produkt_wybrany}]: "))
        if magazyn[produkt_wybrany] < waga:
            print(f"Mamy za mało [{produkt_wybrany}], pozostało {magazyn[produkt_wybrany]} kg")
            continue
        magazyn[produkt_wybrany] = magazyn[produkt_wybrany] - waga
        cena = produkty[produkt_wybrany]
        koszt = waga * cena
        # if produkt_wybrany in koszyk:
        #     koszyk[produkt_wybrany] = koszyk[produkt_wybrany] +  koszt
        # else:
        #     koszyk[produkt_wybrany] = koszt
        koszyk[produkt_wybrany] = koszyk.get(produkt_wybrany, 0) + koszt

        # do_zaplaty += koszt
    elif komenda == 'd':
        # dodawanie do magazynu
        produkt_do_dodania = input("Jaki produkt chcesz dodać? ")
        if produkt_do_dodania not in magazyn:
            magazyn[produkt_do_dodania] = 0
            cena_nowego_produktu = float(input("Za ile to sprzedajemy? "))
            produkty[produkt_do_dodania] = cena_nowego_produktu

        ile_produktu_dodajemy = float(input("Ile tego dodać? "))
        magazyn[produkt_do_dodania] += ile_produktu_dodajemy
    else:
        print("Niepoprawna komenda!!")

print("="*40)
print(f"Za zakupy zapłacisz: ")
suma = 0
for product in koszyk:
    print(f" - {product} - {koszyk[product]} PLN")
    suma += koszyk[product]

print("-"*40)
print(f"Suma: {suma} PLN")




