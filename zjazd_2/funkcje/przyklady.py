# def drukuj_linie():
#     print("-"*40)
#
#
# def zwroc_wartosc_wpisana():
#     wartosc = input("Podaj wartosc")
#     return wartosc
#
# a = [1,2,3,4,5]
#
# def zwroc_sume_zdefiniowanej_listy(a):
#     b = 1
#     print("poziom 1", locals())
#     print("poziom 1", globals())
#     a.append(b)
#     def funkcja_wewnetrzna():
#         c=1
#         print("poziom 2", locals())
#         print("poziom 2", globals())
#         print("b", b)
#     funkcja_wewnetrzna()
#     # a = [5,6,7]
#     return sum(a)
#
#
# # print("poziom 0", locals())
# # print("poziom 0", globals())
# #
# # print("lista a przed wywołaniem", a)
# # print(zwroc_sume_zdefiniowanej_listy([]))
# # print("lista a po wywołaniu", a)
# #
#
# def kalkulator(a, b, operacja='+', opis=""):
#     """Działa na dwóch liczbach. Domyślnie je sumuje"""
#     if opis:
#         print(opis)
#     if operacja == "+":
#         return a+b
#     elif operacja == "-":
#         return a-b
#
# #'ala [kota [a kot]] ma [ale]',
# # 0000 11111 22222  0000 111
#
#
# print(kalkulator(1, 2, opis="dodawanie dwóch liczb"))
#
# print(kalkulator(1, 2, "-"))
#
# print(kalkulator(1, 2, "-", "Odejmowanie dwóch liczb"))
#
#
# def foo(a):
#     b = ""
#     if a > 2:
#         b="haha"
#     print(b)

#
# def foo2(x, *args , **kwargs ):
#     # print("cena", x)
#     # print("args", args)
#     # print("kwargs", kwargs)
#
#     for text in args:
#         print(text)
#
#     for key in kwargs:
#         print(key, kwargs[key])
#
# x = ["tekst 1 $cena", "tekst 2 $cena", "tekst 3 $cena"]
# slownik = {'cena':10, 'podatek':0.23}
#
# foo2(10, *x, **slownik)

def podzielna_przez_2(x):
    return x%2 == 0


print(podzielna_przez_2(12))
print(podzielna_przez_2(11))

# y = lambda x: x%2 == 0
y = podzielna_przez_2
print(y(4))
print(y(5))

def wieksz_niz_7(x):
    if x>7:
        return True
    return False

def wybierz(dane, warunek):
    """

    :param dane: lista liczb
    :param warunek: jakas funkcja sprawdzajaca cos
    :return: przefiltrowana lista
    """
    out = []
    for element in dane:
        if warunek(element):
            out.append(element)
    return(out)

def podzielna_przez_3(x):
    return x%3 == 0

lista = [1,2,3,4,5,6,7,8,9,122,123]
print(wybierz(lista, podzielna_przez_2 ))
print(wybierz(lista, wieksz_niz_7 ))
print(wybierz(lista, lambda x: x%3 == 0 ))
print(wybierz(lista, podzielna_przez_3 ))