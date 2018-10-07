
# # zebranie liczb (nie więcej niż 10)
#
# liczby = input("Prosze podać liczby, rozdzielając je przecinkami:\n")
# liczby = liczby.split(",")
# if len(liczby) > 10:
#     liczby = liczby[:10]
# # i=0
# # suma = 0
# # while i < len(liczby):
# #     suma = suma + int(liczby[i])
# #     i += 1
#
# for liczba in liczby:
#     suma = suma + int(liczba)



liczby = []

while len(liczby) < 10:
    dane = input("Proszę podać liczbę, lub [k] by zakończyć: ")
    if dane == 'k':
        break
    nowa_liczba = int(dane)
    liczby.append(nowa_liczba)
# obliczenie średniej
srednia = sum(liczby)/len(liczby)

# wypisanie wyniku
print(srednia)