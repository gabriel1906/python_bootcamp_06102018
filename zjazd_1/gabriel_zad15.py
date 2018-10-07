from random import randint

# losowanie położenia

s_x = randint(1, 10)
s_y = randint(1, 10)
g_x = randint(1, 10)
g_y = randint(1, 10)

min_liczba_krokow = abs(s_x - g_x) + abs(s_y - g_y)

while True:
    min_liczba_krokow_przed = abs(s_x - g_x) + abs(s_y - g_y)

    ruch = input("wykonaj ruch [wsda]: ")
    ruch = ruch.lower()

    if ruch == 'w':
        g_y += 1

    if ruch == 's':
        g_y -= 1

    if ruch == 'd':
        g_x += 1

    if ruch == 'a':
        g_x -= 1

    min_liczba_krokow_po = abs(s_x - g_x) + abs(s_y - g_y)

    if min_liczba_krokow_po > min_liczba_krokow_przed:
        print("zimno")

    if min_liczba_krokow_po < min_liczba_krokow_przed:
        print("ciepło")

    if (s_x == g_x) and (s_y == g_y):
        print("Znalazłeś skarb")
        break

    if g_x > 10 or g_y > 10:
        print("wypadłeś z planszy")
        break

    if g_x < 1 or g_y < 1:
        print("wypadłeś z planszy")
        break

print(f"Połoźenie skarbu: x={s_x}, y={s_y}")

print(f"Połoźenie gracza: x={g_x}, y={g_y}")

print(min_liczba_krokow)