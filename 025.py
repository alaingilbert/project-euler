i = a = b = 1
while True:
   a, b, i = b, a + b, i + 1
   if len(str(a)) >= 1000: break
print i
