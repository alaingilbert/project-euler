from math import ceil

def is_prime(n):
   if n < 2: return False
   if n == 2: return True
   if n % 2 == 0: return False
   for i in range(3, int(ceil(n ** 0.5))+1, 2):
      if n % i == 0: return False
   return True

def gen():
   yield 2
   it = 3
   while True:
      if is_prime(it): yield it
      it += 2

def rot(n):
   s = str(n)
   return [ int(s[i:]+s[:i])  for i in range(0, len(s)) ]

r = []
g = gen()
p = g.next()
while p < 1000000:
   find = False
   for j in rot(p):
      if not is_prime(j):
         find = True
         break
   if not find: r.append(p)
   p = g.next()

print len(r)
