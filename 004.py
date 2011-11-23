def is_palindrome(n):
   s = str(n)
   i = len(s)/2
   while i < len(s):
      if s[i] != s[-(i+1)]:
         return False
      i += 1
   return True

max = 0
for i in range(100, 1000):
   for j in range(100, 1000):
      if is_palindrome(i * j):
         if i * j > max: max = i * j

print max
