def fact(n):
   v = 1
   for i in range(1, n+1): v *= i
   return v

s = str(fact(100))
sum = 0
for i in range(len(s)): sum += int(s[i])
print sum
