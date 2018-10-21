# To jest program liczący pole trapezu
a = 3 # zmienna a
b = 9
h = 6.5
"""
To jest wielolinijkowy komentarz
bla 
bla bla
"""
pole_trapezu = ((a + b) / 2) * h # wzor na pole trapezu

assert pole_trapezu == 39.0

print(f"Pole trapezu o podstawach: {a}, {b} i wysokości: {h} wynosi: {pole_trapezu}")
print("Pole trapezu o podstawach: {}, {} i wysokości: {} wynosi: {}".format(a,b,h, pole_trapezu))


