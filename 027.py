from math import ceil

def is_prime(n):
   if n < 2: return False
   if n == 2: return True
   if n % 2 == 0: return False
   for i in range(3, int(ceil(n ** 0.5))+1, 2):
      if n % i == 0: return False
   return True

a = b = 0
e = lambda n: n**2 - a*n + b

s = { 'nb':0, 'a':0, 'b':0 }

for i in range(0, 1000):
   for j in range(0, 1000):
      a, b, nb = i, j, 0
      while True:
         if not is_prime(e(nb)):
            if nb-1 > s['nb']:
               s['nb'] = nb-1
               s['a'] = a
               s['b'] = b
            break
         nb += 1

print -s['a'] * s['b']
