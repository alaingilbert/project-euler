import urllib2
a = [ i.replace('"', '') for i in urllib2.urlopen('http://projecteuler.net/project/names.txt').read().split(',') ]
a.sort()
def pts(name): return sum([ ord(i) - 64 for i in name ])
print sum([ (pos+1) * pts(name) for pos, name in enumerate(a) ])
