import urllib2, re

a = urllib2.urlopen('http://projecteuler.net/project/cipher1.txt').read().split(',')
a[len(a)-1] = a[len(a)-1].replace('\r\n', '')
a = [ int(x) for x in a]

def psw_gen():
   for a in range(97, 123):
      for b in range(97, 123):
         for c in range(97, 123):
            psw = [a, b, c]
            yield psw


max = { 'count': 0, 'psw': [] }
c = 0
for psw in psw_gen():
   if c % 1000 == 0: print 'Progress: %d%%' % (c / (26.0 ** 3) * 100)
   c += 1
   tmp = [ x for x in a ]
   for i, e in enumerate(tmp):
      tmp[i] = e ^ psw[ i % len(psw) ]
   sa = ''.join( [ chr(x) for x in tmp ] )
   d = re.findall('the', sa, re.I)
   if len(d) > max['count']: max = { 'count': len(d), 'psw': psw }

print 'Password: %s' % (chr(max['psw'][0]) + chr(max['psw'][1]) + chr(max['psw'][2]))

txt = ''.join( [ chr(e ^ max['psw'][ i % len(max['psw']) ]) for i, e in enumerate(a) ] )
print 'Text: %s' % txt

sum = 0
for i in txt: sum += ord(i)
print 'Response: %s' % sum
