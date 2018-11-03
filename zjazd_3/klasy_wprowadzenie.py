x = 1
napis = "To jest napis"
y = 1.2
slownik = {}

def foo():
    pass

print(type(x), type(y), type(napis), type(slownik), type(None), type(foo))
print(dir(x))


# definicja klasy
class Animal:
    nazwa = "Fauna"  # atrybut klasowy
    licznik = 0
    instances = []

    def __init__(obiekt, gatunek):
        obiekt.gatunek = gatunek  # atrybuty instancji, obiektu
        obiekt.stan = "nic nie robi"
        obiekt.pasza = None
        obiekt.zwieksz_licznik()
        obiekt.add_to_instances(obiekt)

    def __str__(obiekt):
        return "Animal"

    def idz(obiekt):
        obiekt.stan = "Idzie"

    def stoj(obiekt):
        obiekt.stan = "Stoi"

    def spij(obiekt):
        obiekt.stan = "Śpi"

    @classmethod
    def zwieksz_licznik(cls):
        cls.licznik += 1

    @classmethod
    def add_to_instances(cls, instance):
        cls.instances.append(instance)


class LeniweZwierzeta(Animal):

    def idz(obiekt):
        obiekt.stan = "Leży"
        return "Chyba żartujesz"

    def show_everything(self):
        print(locals())
        print(globals())


# tworzenie instancji danej klasy
azor = Animal("Canis Familiaris")
rudolf = Animal("Rangifer tarandus")

print(azor)  # reprezentacja napisowa instancji mojej klasy
# print(type(azor))
# print(dir(azor))
print(azor.gatunek)  # wypisanie atrybutu
print(rudolf.gatunek)
print(azor.nazwa)
print(rudolf.nazwa)

Animal.nazwa = "flora"
print(azor.nazwa)
print(rudolf.nazwa)

azor.gatunek = "Canis Lupus"
print(azor.gatunek)
print(rudolf.gatunek)

print(dir(azor))

azor.idz()
print("Azor stan: ", azor.stan)
garfield = LeniweZwierzeta("Felis catus")

print(dir(garfield))
garfield.idz()

print("Garfield stan: ", garfield.stan)
print(garfield.__dict__)
print(LeniweZwierzeta.instances)