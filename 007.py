def is_prime(n):
   if n < 2:      return False
   if n % 2 == 0: return False
   for i in range(2, n/2):
      if n % i == 0: return False
   return True

i = 2
n = 1
while True:
   if is_prime(i): n += 1
   if n == 10001: break
   i += 1
print i
