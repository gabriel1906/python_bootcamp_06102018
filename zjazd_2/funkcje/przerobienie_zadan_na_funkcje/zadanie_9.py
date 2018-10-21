import datetime
now = datetime.datetime.now()

print(now.year)
print(now.month)

rok_urodzenia = int(input("Podaj rok urodzenia: "))

wiek = now.year - rok_urodzenia

if wiek >= 18:
    print("Jesteś pełnoletni")
else:
    print("Przykro mi nie może kupić alkoholu")

