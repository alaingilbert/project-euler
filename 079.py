import urllib2
t = urllib2.urlopen('http://projecteuler.net/project/keylog.txt').read().strip().split('\r\n')

numbers = []

for i in t:
   for c in i:
      if c not in numbers:
         numbers.append(c)

tmp = {}
for i in numbers:
   tmp[i] = set()

for i in t:
   f, s, l = i[0], i[1], i[2]
   tmp[f].add(s)
   tmp[f].add(l)
   tmp[s].add(l)

a = [ (i, len(tmp[i])) for i in tmp ]
a = sorted(a, key=lambda x: x[1], reverse=True)
s = ''.join(i for i, x in a)
print s
