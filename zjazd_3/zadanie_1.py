class Product(object):
    def __init__(self, id, nazwa, cena):
        self.ID = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        return f'Produkt "{self.nazwa}", id: {self.ID}, cena: {self.cena} PLN'


def test_product():
    product = Product(1, 'Woda', 10.99)

    assert hasattr(product, "ID")
    assert hasattr(product, "nazwa")
    assert hasattr(product, "cena")

    assert product.ID == 1
    assert product.nazwa == "Woda"
    assert product.cena == 10.99

def test_product_print_info():
    product = Product(1, 'Woda', 10.99)
    assert product.print_info() == 'Produkt "Woda", id: 1, cena: 10.99 PLN'
