a = int(input("Podaj a"))
b = int(input("Podaj b"))

if a > b and a % b == 0:
    print(f"liczba {a} jest większa od {b} i jest przez {b} podzielna")
elif a == b:
    print(f"liczba a jest równa b i wynosi: {a}")
else:
    print("Haha")

print("Bbbb")