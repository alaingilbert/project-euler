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

def is_pandigital(n):
   n = str(n)
   for i in range(1, len(n)+1):
      if not str(i) in n: return False
   return True


g = gen()
p = g.next()
l = 0
while p < 8000000:
   if is_pandigital(p) and p > l: l = p
   p = g.next()

print l
