a = [1]
for i in range(1, 9): a.append(a[i-1] * (i+1))
a.reverse()

s = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
f = []
n = 999999
c = it = 0
while n > 0:
   if n >= a[it]:
      n -= a[it]
      c += 1
   if n < a[it]:
      f.append(s.pop(c))
      it += 1
      c = 0
f.append(s.pop(c))

print ''.join(f)
