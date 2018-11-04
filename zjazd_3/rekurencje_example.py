
# 10! = 1*2*3*4*5*6*7*8*9*10

def silnia(liczba):
    if liczba == 0:
        return 1
    return liczba*silnia(liczba-1)


print(silnia(900))
