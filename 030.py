n, s = 2, []
while True:
   t = sum([ int(i) ** 5 for i in str(n) ])
   if t == n: s.append(n)
   n += 1
   if n > 1000000: break
print sum(s)
