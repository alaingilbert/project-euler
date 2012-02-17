months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
idx, sum = 0, 0
for y in range(1900, 2001):
   for m in range(0, 12):
      days = months[m]
      if m == 1 and y % 4 == 0:
         if y % 100 == 0 and not y % 400: days = 28
         else: days = 29
      for d in range(0, days):
         if y >= 1901 and d == 0 and idx == 0: sum += 1
         idx = 0 if (idx + 1) % 7 == 0 else idx + 1
print sum
