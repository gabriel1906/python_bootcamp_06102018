
print("Podaj wymiary [cm]: ")
a = int(input())
b = int(input())
c = int(input())

if a*b*c > 1000:
    print("Objętość przekroczyła litr")
else:
    print("Objętość mniejsza lub równa litrowi")

