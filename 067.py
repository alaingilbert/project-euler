import urllib2

s = urllib2.urlopen('http://projecteuler.net/project/triangle.txt').read().strip()

arr = s.split("\r\n")
for i in range(len(arr)): arr[i] = arr[i].split(" ")
for i in range(len(arr)):
   for j in range(len(arr[i])):
      arr[i][j] = int(arr[i][j])

for i in range(len(arr) - 1, 0, -1):
   for j in range(len(arr[i])-1):
      if arr[i][j] + arr[i-1][j] > arr[i][j+1] + arr[i-1][j]:
         arr[i-1][j] += arr[i][j]
      else:
         arr[i-1][j] += arr[i][j+1]

print arr[0][0]
