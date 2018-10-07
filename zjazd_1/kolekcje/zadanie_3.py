lista = [-1, 100, 20, 30, -15, 0, 200, -1000]

# 1. liczniki

licznik_ujemnych = 0
licznik_dodatnich = 0

for el in lista:
    if el < 0:
        licznik_ujemnych += 1
    elif el > 0:
        licznik_dodatnich += 1

# 2. na listach

dodatnie = []
ujemne = []

for el in lista:
    if el < 0:
        dodatnie.append(el)
    elif el > 0:
        ujemne.append(el)


# wydrukuj wyniki

print("Dodatnich: ", licznik_dodatnich)
print("Ujemnych: ", licznik_ujemnych)

print("Dodatnich: ", len(dodatnie))
print("Ujemnych: ", len(ujemne))

