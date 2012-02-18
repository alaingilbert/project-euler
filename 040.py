n, s = 0, ''
while len(s) < 1000000:
   n += 1
   s += str(n)
print int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])
