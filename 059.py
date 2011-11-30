import urllib2, re

a = [ int(x) for x in  urllib2.urlopen('http://projecteuler.net/project/cipher1.txt').read().split(',') ]

def psw_gen():
   for a in range(97, 123):
      for b in range(97, 123):
         for c in range(97, 123):
            yield [ a, b, c ]

max = { 'count': 0, 'psw': [] }
c = 0
for psw in psw_gen():
   if c % 1000 == 0: print 'Progress: %d%%' % (c / (26.0 ** 3) * 100)
   c += 1
   sa = ''.join( [ chr(e ^ psw[ i % len(psw) ]) for i, e in enumerate(a) ] )
   d = re.findall('the', sa, re.I)
   if len(d) > max['count']: max = { 'count': len(d), 'psw': psw }

print 'Password: %s' % (chr(max['psw'][0]) + chr(max['psw'][1]) + chr(max['psw'][2]))

txt = ''.join( [ chr(e ^ max['psw'][ i % len(max['psw']) ]) for i, e in enumerate(a) ] )
print 'Text: %s' % txt

sum = 0
for i in txt: sum += ord(i)
print 'Response: %s' % sum
