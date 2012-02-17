from math import ceil

def is_prime(n):
   if n < 2:      return False
   if n == 2:     return True
   if n % 2 == 0: return False
   for i in range(3, int(ceil(n ** 0.5)) + 1, 2):
      if n % i == 0: return False
   return True


def next_prime():
   n = 2
   while True:
      if is_prime(n):
         yield n
      n += 1


def prime_factors(c):
   gen = next_prime()
   p = gen.next()
   a = []
   while c > 1:
      if c % p == 0:
         c = c / p
         a.append(p)
      else:
         p = gen.next()

   return a


def count_divisors(a):
   tmp, e, c = [], a[0], 0
   for i in a:
      if i == e: c += 1
      if i != e:
         tmp.append(c)
         e, c = i, 1
   tmp.append(c)
   s = 1
   for i in tmp: s *= i+1
   return s


c, i, p = 1, 1, 0
while True:
   i += 1
   c += i
   if c > p:
      p += 1000000
      print 'Progress: %s' % c
   if count_divisors(prime_factors(c)) > 500:
      break

print c
