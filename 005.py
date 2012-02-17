n = 20
while True:
   n += 20
   f = False
   for i in range(2, 21):
      if n % i != 0:
         f = True
         break
   if n % 1000000 == 0: print "Progress: %s" % n
   if f: continue
   else: break
print 'Result: %s' % n
