a, s, n = [1], ['0','1','2','3','4','5','6','7','8','9'], 999999
c = it = 0
for i in range(2, 10): a.insert(0, a[0] * i)
while n > 0:
   if n >= a[it]: n, c = n-a[it], c+1
   if n < a[it]:
      s.insert(it, s.pop(c + it))
      it, c = it+1, 0
print ''.join(s)
