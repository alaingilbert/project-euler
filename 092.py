max, sum, c, bc = 10000000, 0, {}, {}
for n in range(2, max):
   if n % 10000 == 0: print 'Progress: %d%%' % (n / (max+0.0) * 100)
   nn = n
   steps = []
   while True:
      steps.append(nn)
      if nn == 1 or bc.get(nn):
         for x in steps: bc[x] = True
         break
      if nn == 89 or c.get(nn):
         for x in steps: c[x] = True
         sum += 1
         break
      s = str(nn)
      nnn = 0
      for i in s: nnn += int(i) ** 2
      nn = nnn
print sum
