from math import ceil

def d(n):
   a = []
   for i in range(1, int(ceil(n ** 0.5))):
      if n % i == 0:
         a.append(i)
         if i != 1:
            a.append(n/i)
   return sum(a)

s = 0
for i in range(2, 10000):
   a = d(i)
   b = d(a)
   if i == a: continue
   if b == i: s += i

print 'Result: %s' % s
