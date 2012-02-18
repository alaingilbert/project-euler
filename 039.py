def f():
   a, c = [], []
   for i in range(1, 1000):
      for j in range(1, 1000):
         if j in c: continue
         tmp = (i*i + j*j) ** 0.5
         if tmp == int(tmp):
            a.append((i, j, int(tmp)))
            c.append(i)
   return a

all = f()


max = 0
s = 0
for p in range(1, 1000):
   if p % 100 == 0: print 'Progress: %s' % p
   r = [] 
   for a, b, c in all:
      if a + b + c == p:
         r.append((a, b, c))
   t = len(r)
   if t > max:
      max = t
      s = p

print s, max
