# napis = "To jest napis mama"
#         #012
#
# print('mama' in napis)
# print(napis[1:10:2])
#
# for litera in napis:
#     print(litera)
#
# print(dir(napis))
# lista = [1,2,3]
# lista[0] # 1
#
# Słowniki
## ctr + / # komentowanie w pycharm

my_dict = {
    "pierwsza": "a",
    "druga": "b"
}
my_dict['trzecia'] = 'c'

d2 = dict()
d2 = dict([('a', 1), ('b', 2)])
print('d2: ', d2)

print(my_dict['druga'])
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

produkt1 = {'nazwa': "Koper", "cena": 3}
produkt2 = {'nazwa': "Kasza", "cena": 1.99}

produkty = [produkt1, produkt2]

print("Produkty w lodówce: ")
for p in produkty:
    print(p['nazwa'])


for k in produkt1:
    print(k, produkt1[k])