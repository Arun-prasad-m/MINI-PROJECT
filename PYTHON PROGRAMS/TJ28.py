a=(1,2.5,True,"ram")
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
b=list(a)
print(b)
b.append("raja")
print(b)
print(type(b))
a=tuple(b)
print(a)
print(type(a))
print("-----------------------")
for i in a:
    print(i)
if "raj" in a:
    print("raja is found")
else:
    print("not found")
print(len(a))
a=(1,)
print(type(a))
del a
a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
c = a + b
print(c)
print(c.count(7))