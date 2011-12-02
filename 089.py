def num(r):
   r = r[::-1]
   a = []
   for i in r:
      if   i == 'M': t = 1000
      elif i == 'D': t = 500
      elif i == 'C': t = 100
      elif i == 'L': t = 50
      elif i == 'X': t = 10
      elif i == 'V': t = 5
      elif i == 'I': t = 1
      a.append(t)
   return a


def r2d(n):
   a = num(n)
   s = i = 0
   while i < len(a):
      if i < len(a)-1 and a[i] > a[i+1]:
         s += a[i] - a[i+1]
         i += 2
         continue
      s += a[i]
      i += 1
   return s


def d2r(n):
   s = ''
   while n > 0:
      if   n >= 900 and n < 1000: s, n = s+'CM', n-900
      elif n >= 400 and n < 500:  s, n = s+'CD', n-400
      elif n >= 90  and n < 100:  s, n = s+'XC', n-90
      elif n >= 40  and n < 50:   s, n = s+'XL', n-40
      elif n >= 9   and n < 10:   s, n = s+'IX', n-9
      elif n >= 4   and n < 5:    s, n = s+'IV', n-4

      elif n >= 1000: s, n= s+'M', n-1000
      elif n >= 500:  s, n= s+'D', n-500
      elif n >= 100:  s, n= s+'C', n-100
      elif n >= 50:   s, n= s+'L', n-50
      elif n >= 10:   s, n= s+'X', n-10
      elif n >= 5:    s, n= s+'V', n-5
      elif n >= 1:    s, n= s+'I', n-1
   return s

import urllib2
s, a = 0, urllib2.urlopen('http://projecteuler.net/project/roman.txt').read().split('\r\n')
for e in a: s += len(e)-len(d2r(r2d(e)))
print s
