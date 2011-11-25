a, s, n, c, i = [1], ['0','1','2','3','4','5','6','7','8','9'], 999999, 0, 0
for x in range(2, 10): a.insert(0, a[0] * x)
while n > 0:
   if n >= a[i]: n, c = n-a[i], c+1
   if n < a[i]:
      s.insert(i, s.pop(c + i))
      i, c = i+1, 0
print ''.join(s)
