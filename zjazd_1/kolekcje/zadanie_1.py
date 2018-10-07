moja_tupla = (2, 5, 7, 1, 2, 3, 6, 8, 9, 12)

assert 5 == moja_tupla[1]
assert 9 == moja_tupla[-2]
assert (7, 1, 2, 3, 6) == moja_tupla[2:7]
assert (2, 1, 6, 12) == moja_tupla[::3]
assert (12, 8, 3, 1, 5) == moja_tupla[::-2]
