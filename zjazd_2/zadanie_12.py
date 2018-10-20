liczby = [5,2,1,4,3]

print("Przed: ", liczby)

for i in range(len(liczby)):
    index_minium = i
    # print('i: ', i, 'liczby: ', liczby[i:])
    for j in range(i+1, len(liczby)):
        if liczby[j] < liczby[index_minium]:
            index_minium = j
    liczby[i], liczby[index_minium] = liczby[index_minium], liczby[i]
    print('i: ', i, 'liczby:', liczby)
print("Po: ", liczby)
