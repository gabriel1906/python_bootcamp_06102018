#pole_trapezu = ((a + b) / 2) * h # wzor na pole trapezu

def pole_trapezu(a, b, h):
    """
    Liczy pole trapezu

    :param a: podstawa 1 - numeric
    :param b: podstawa 2 - numeric
    :param h: wysokosc   - numeric
    :return: pole powierzchni - numeric
    """
    return ((a + b) / 2) * h


def test_pole_trapezu():
    assert pole_trapezu(3, 9, 6.5) == 39.0

#print(f"Pole trapezu o podstawach: {a}, {b} i wysokości: {h} wynosi: {pole_trapezu}")
#print("Pole trapezu o podstawach: {}, {} i wysokości: {} wynosi: {}".format(a,b,h, pole_trapezu))


