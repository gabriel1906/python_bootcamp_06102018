zbior = {1,2,3,4,1}
print(zbior)
zbior.add(1)
zbior.add("a")
print(zbior)
print(1 in zbior)
print(6 in zbior)

for i in zbior:
    print(i)

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) # suma
print(a.union(b))
print(a - b) # różnica
print(a.difference(b))
print(a & b) # część wsp - iloczyn
print(a.intersection(b))
print(a ^ b) # różnica symetryczna
print(a.symmetric_difference(b))
print(dir(a))

print(set([1,2,3,4,5,1]))
print(set(range(1, 10)))