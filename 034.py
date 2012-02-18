from math import factorial
a = []
for i in range(3, 1000000):
   if sum([ factorial(int(j)) for j in str(i) ]) == i: a.append(i)
print sum(a)
