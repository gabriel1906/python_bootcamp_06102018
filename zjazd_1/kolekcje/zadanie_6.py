liczby = [5, 2, 1, 4, 3]


indeksy = list(range(len(liczby)))

min_i, max_i = None, None

for i in indeksy:
    if min_i == None or liczby[i] < liczby[min_i]:
        min_i = i
    if max_i == None or liczby[i] > liczby[max_i]:
        max_i = i

# if min_i is not None and max_i is not None:
#     tmp = liczby[min_i]          # przechowuje wartość z indeksu min_i
#     liczby[min_i] = liczby[max_i]
#     liczby[max_i] = tmp
# sposób drugi

liczby[min_i], liczby[max_i] = liczby[max_i], liczby[min_i]

assert liczby == [1, 2, 5, 4, 3]