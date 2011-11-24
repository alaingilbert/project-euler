def find():
   a = b = c = 1
   for i in range(500):
      a = i
      for j in range(500):
         b = j
         for k in range(500):
            c = k
            if a ** 2 + b ** 2 - c ** 2 == 0 and a + b + c == 1000:
               return a * b * c
print find()
