def a(n):
   steps = 1
   while n > 1:
      if n % 2 == 0: n /= 2
      else: n = 3*n + 1
      steps += 1
   return steps

num = 0
max = 0
for i in range(1, 1000000):
   s = a(i)
   if i % 100000 == 0: print 'Progress: %s' % i
   if s > max: max, num = s, i

print 'Result: %s' % num
