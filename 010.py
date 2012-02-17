from math import ceil

def is_prime(n):
   if n < 2:      return False
   if n % 2 == 0: return False
   for i in range(3, int(ceil(n ** 0.5)) + 1, 2):
      if n % i == 0: return False
   return True

sum = 2
for i in range(3, 2000000, 2):
   if i % 100001 == 0: print 'Progress: %s' % i
   if is_prime(i): sum += i
print 'Result: %s' % sum
