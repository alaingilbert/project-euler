import urllib2
a = map(lambda x: x.replace('"', ''), urllib2.urlopen('http://projecteuler.net/project/words.txt').read().split(','))

c = []
i = t = 1
while t <= 192:
   t = i * (i+1)/2
   i += 1
   c.append(t)

def word_value(s):
   sum = 0
   for i in range(len(s)): sum += ord(s[i]) - 64
   return sum

def is_triangle(n): return n in c

s = 0
for i in range(len(a)):
   if is_triangle(word_value(a[i])): s += 1

print s
