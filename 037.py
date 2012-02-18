from math import ceil

def is_prime(n):
   if n < 2: return False
   if n == 2: return True
   if n % 2 == 0: return False
   for i in range(3, int(ceil(n ** 0.5))+1, 2):
      if n % i == 0: return False
   return True

def gen():
   it = 9
   while True:
      if is_prime(it): yield it
      it += 2

def trunk(n):
   s = str(n)
   a = [n]
   for i in range(1, len(s)):
      a.append(int(s[i:]))
      a.append(int(s[:i]))
   return a

n = 0
g = gen()
r = []
while True:
   p = g.next()
   find = False
   for i in trunk(p):
      if not is_prime(i):
         find = True
         break

   if not find:
      r.append(p)
      n += 1
   if n == 11: break

print sum(r)
