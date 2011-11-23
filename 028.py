n = 1
step = 1
sum = 0
l = 1001
i = 1
while i < l ** 2 + 1:
   if i == n ** 2:
      n += 2
      step = n - 1
   sum += i
   i += step

print sum
