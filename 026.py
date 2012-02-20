max, c = 0, 0
for n in xrange(999, 0, -1):
   if n-1 < max: break
   rs, r = [], 1 % n
   rs.append(r)
   while True:
      r = (r*10) % n
      if r in rs: break
      rs.append(r)
   l = len(rs[rs.index(r):])
   if l > max: max, c = l, n
print c
