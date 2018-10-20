my_text = input("Podaj tekst: ")

# Sposob 1
nawias1 = 0
nawias2 = 0

for index, i in enumerate(my_text):
    if i == "<":
       nawias1 = index
    if i == ">":
       nawias2 = index

print(nawias2 - nawias1-1)

# spsob 2
czy_miedzy_nawiasami = False
licznik = 0

for znak in my_text:
    if znak == "<":
        czy_miedzy_nawiasami = True
    elif znak == ">":
        czy_miedzy_nawiasami = False
    elif czy_miedzy_nawiasami:
        licznik += 1

print(licznik)