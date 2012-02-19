from decimal import *
getcontext().prec = 102
sqr = [ i*i for i in range(1, 11) ]
s = 0
for n in xrange(1, 101):
   if n in sqr: continue
   t = str(int(Decimal(n).sqrt()*10**99))
   s += sum( int(i) for i in t )
print s
