from random import randint

sx = randint(1, 10)
sy = randint(1, 10)
gx = randint(1, 10)
gy = randint(1, 10)
odleglosc_min = abs(sx - gx) + abs(sy - gy)
poczatkowa_lr = 0

while True:
    odleglosc_przed = abs(sx - gx) + abs(sy - gy)
    ruch = input("Podaj ruch (WSAD): ")
    ruch = ruch.upper()

    if ruch == 'W':
        gy = gy + 1

    elif ruch == "S":
        gy = gy - 1

    elif ruch == "A":
        gx = gx - 1

    elif ruch == "D":
        gx = gx + 1

    # wyjście poza planszę
    if gx > 10 or gx < 1 or gy > 10 or gx < 1:
        print("Wyszedłeś poza planszę")
        break

    odleglosc_teraz = abs(sx - gx) + abs(sy - gy)

    if odleglosc_teraz < odleglosc_przed:
        print(f"Cieplo skarb {sx},{sy}. Ty {gx},{gy}")

    elif odleglosc_teraz > odleglosc_przed:
        print(f"Zimno skarb {sx},{sy}. Ty {gx},{gy}")

    # koniec gry = sukces
    if sx == gx and sy == gy:
        break

print("!!!")
