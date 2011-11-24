d = {}
for i in range(2, 101):
   for j in range(2, 101):
      d[i ** j] = True
print len(d)
