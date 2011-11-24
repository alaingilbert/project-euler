i = n = s = 1
while i < 1001 ** 2 + 1:
   if i == n ** 2: n += 2
   s, i = s + i, i + n - 1
print s - 1
