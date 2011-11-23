n = 600851475143
d = 2
while n > 1:
   if n % d == 0:
      n /= d
      d -= 1
   d += 1
print d
