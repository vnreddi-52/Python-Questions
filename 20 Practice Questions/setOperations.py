a = {1,2,3,4}
b = {3,4,5,6}
c = a.union(b)
d= a | b

e = a & b
f = a.intersection(b)

a1 = a-b
a2= a.difference(b)

b1= a.symmetric_difference(b)
b2 = a^b
print(c,a1,a2,b1,b2)