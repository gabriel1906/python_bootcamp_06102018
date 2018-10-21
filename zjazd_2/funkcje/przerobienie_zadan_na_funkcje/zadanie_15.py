from random import randint


def losuj_polozenie():
    return randint(1, 10), randint(1, 10)


def minimalna_liczba_krokow(gracz_x, gracz_y, skarb_x, skarb_y):
    return abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)


def zmiana_pozycji_gracza(gracz_x, gracz_y, liczba_ruchow):
    out = False
    ruch = input("Wykonaj ruch [wasd]: ")
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

    liczba_ruchow += 1

    if gracz_x > 10 or gracz_y > 10 or gracz_x < 1 or gracz_y < 1:
        print("Wyszedłeś poza planszę")
        out = True

    return gracz_x, gracz_y, liczba_ruchow, out


def sprawdzenie(min_l_ruch_po, min_l_ruch_przed):
    # sprawdzamy czy znalazł skarb
    if min_l_ruch_po == 0:
        print("Wygrałeś")
        return True
    # określenie czy się przybliża czy oddala
    if min_l_ruch_po > min_l_ruch_przed:
        print("Zimno")
    if min_l_ruch_po < min_l_ruch_przed:
        print("Ciepło")


skarb_x, skarb_y = losuj_polozenie()
gracz_x, gracz_y = losuj_polozenie()

print("Skarb", skarb_x, skarb_y)
print("Gracz", gracz_x, gracz_y)
# oblicz minimalna liczbę kroków między graczem a skarbem
minimalna_liczba_krokow_po_wylosowaniu = minimalna_liczba_krokow(gracz_x, gracz_y, skarb_x, skarb_y)
# zapisz w zmiennej

# ustaw początkowa liczbę ruchów na 0
liczba_ruchow = 0

# mechanika
while True:
    # oblicz minimalna liczba krokow przed ruchem
    min_l_ruch_przed = minimalna_liczba_krokow(gracz_x, gracz_y, skarb_x, skarb_y)
    gracz_x, gracz_y, liczba_ruchow, out = zmiana_pozycji_gracza(gracz_x, gracz_y, liczba_ruchow)
    if out:
        break

    # oblicz minimalna liczbe krokow po ruchu
    min_l_ruch_po = minimalna_liczba_krokow(gracz_x, gracz_y, skarb_x, skarb_y)
    wynik = sprawdzenie(min_l_ruch_po, min_l_ruch_przed)
    if wynik:
        break

    if liczba_ruchow > 2 * minimalna_liczba_krokow_po_wylosowaniu:
        # wylosuj położenie skarbu
        skarb_x, skarb_y = losuj_polozenie()

        # oblicz minimalna liczbę kroków między graczem a skarbem
        minimalna_liczba_krokow_po_wylosowaniu = minimalna_liczba_krokow(gracz_x, gracz_y, skarb_x, skarb_y)

print(f"Położenie skarbu: x={skarb_x}, y={skarb_y}")
print(f"Położenie gracza: x={gracz_x}, y={gracz_y}")
print(minimalna_liczba_krokow_po_wylosowaniu)
