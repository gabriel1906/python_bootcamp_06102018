

file = open("dane/przykladowy_excel.csv")
print(file.read())
file.close()


with open("dane/przykladowy_excel.csv") as f:
    print(type(f))
    for line in f:
        print(line.lower())


with open("dane/nowy_plik.txt", 'w', encoding='utf8') as f:
    f.write("zażółć gęślą jaźń\n")


with open("dane/nowy_plik.txt", encoding="utf8") as f:
    x = f.read()
    print(type(x))
