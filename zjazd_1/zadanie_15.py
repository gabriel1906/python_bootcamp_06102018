from random import randint

# wylosuj położenie skarbu
skarb_x = randint(1, 10)
skarb_y = randint(1, 10)

# wylosuj początkowe położenie gracza
gracz_x = randint(1, 10)
gracz_y = randint(1, 10)

# oblicz minimalna liczbę kroków między graczem a skarbem
minimalna_liczba_krokow_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y-gracz_y)
# zapisz w zmiennej

# ustaw początkowa liczbę ruchów na 0
liczba_ruchow = 0

# gracz_x, gracz_y = 1, 1
# skarb_x, skarb_y = 1, 1

# mechanika
while True:
    # oblicz minimalna liczba krokow przed ruchem
    min_l_ruch_przed = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    ruch =  input("Wykonaj ruch [wasd]: ")
    # poruszanie gracza po planszy
    # w a s d
    if ruch == 'w':
        gracz_y += 1
    if ruch == 'a':
        gracz_x -= 1
    if ruch == 's':
        gracz_y -= 1
    if ruch == 'd':
        gracz_x += 1

    # powiekszam liczbę ruchów
    liczba_ruchow += 1

    # przerwanie gry gdy wyjdzie poza planszę
    if gracz_x > 10 or gracz_y > 10 or gracz_x < 1 or gracz_y < 1:
        print("Wyszedłeś poza planszę")
        break

    # oblicz minimalna liczbe krokow po ruchu
    min_l_ruch_po = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    # sprawdzamy czy znalazł skarb
    if min_l_ruch_po == 0:
        print("Wygrałeś")
        break

    # określenie czy się przybliża czy oddala
    if min_l_ruch_po > min_l_ruch_przed:
        print("Zimno")
    if min_l_ruch_po < min_l_ruch_przed:
        print("Ciepło")

    if liczba_ruchow > 2 * minimalna_liczba_krokow_po_wylosowaniu:
        # wylosuj położenie skarbu
        skarb_x = randint(1, 10)
        skarb_y = randint(1, 10)
        # oblicz minimalna liczbę kroków między graczem a skarbem
        minimalna_liczba_krokow_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y-gracz_y)


print(f"Położenie skarbu: x={skarb_x}, y={skarb_y}")
print(f"Położenie gracza: x={gracz_x}, y={gracz_y}")
print(minimalna_liczba_krokow_po_wylosowaniu)