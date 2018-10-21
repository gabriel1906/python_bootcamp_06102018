# jest podzielna przez 2, podzielna przez 3 i wieksza od 10 lub jest to
# liczba 7.

liczba = int(input("Podaj liczbę: "))

podzielna_przez_2 = liczba % 2 == 0
podzielna_przez_3 = liczba % 3 == 0
wieksza_niz_10 = liczba > 10
rowna_7 = liczba == 7

# print(podzielna_przez_2, podzielna_przez_3, wieksza_niz_10, rowna_7)

wynik = podzielna_przez_2 and  \
         podzielna_przez_3 and \
         wieksza_niz_10 or rowna_7

print(wynik)
