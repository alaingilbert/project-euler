def bin(n):
   s, r = '', 0
   while n >= 1:
      r = n % 2
      n = n >> 1
      s = str(r) + s
   return s

def is_palindrome(n):
   s = str(n)
   i = len(s)/2
   while i < len(s):
      if s[i] != s[-(i+1)]:
         return False
      i += 1
   return True

a = []
for i in range(0, 1000000):
   if is_palindrome(i):
      b = bin(i)
      if is_palindrome(b):
         a.append(i)

print sum(a)
