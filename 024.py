a = [1]
for i in range(1, 9): a.append(a[i-1] * (i+1))
a.reverse()

s, n = ['0','1','2','3','4','5','6','7','8','9'], 999999
c = it = 0
while n > 0:
   if n >= a[it]: n, c = n-a[it], c+1
   if n < a[it]:
      s.insert(it, s.pop(c + it))
      it, c = it+1, 0

print ''.join(s)
