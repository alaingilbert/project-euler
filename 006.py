v1 = v2 = 0
for i in range(1, 101):
   v1 += i ** 2
   v2 += i
v2 **= 2
print v2 - v1
