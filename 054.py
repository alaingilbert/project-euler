import urllib2
a = [ x.split(' ') for x in urllib2.urlopen('http://projecteuler.net/project/poker.txt').read().split('\r\n')[:-1] ]

def custom_sort(x, y):
   l1, c1, l2, c2 = x[0], x[1], y[0], y[1]
   if l1 == l2: return 0
   if l1 > l2: return 1
   if l1 < l2: return -1

def num_card(c):
   v = c[0]
   if   v == 'T': v = 8
   elif v == 'J': v = 9
   elif v == 'Q': v = 10
   elif v == 'K': v = 11
   elif v == 'A': v = 12
   else: v = int(v) - 2
   return [v, c[1]]

def order_hand(h):
   return sorted([ num_card(x) for x in h ], cmp=custom_sort)

def is_straight(h):
   for i in range(len(h)-1):
      if h[i][0] != h[i+1][0]-1: return False
   return True

def is_flush(h):
   suit = h[0][1]
   for i in range(1, len(h)):
      if h[i][1] != suit: return False
   return True

def is_royal(h):
   if h[0][0] != 8: return False
   for i in range(len(h)-1):
      if h[i][0] != h[i+1][0]-1: return False
   return True

def has_four(h):
   if   h[0][0] == h[1][0] and h[1][0] == h[2][0] and h[2][0] == h[3][0]: return True, [h[0][0], h[4][0]]
   elif h[1][0] == h[2][0] and h[2][0] == h[3][0] and h[3][0] == h[4][0]: return True, [h[1][0], h[0][0]]
   return False, []

def is_full_house(h):
   if   h[0][0] == h[1][0] and h[1][0] == h[2][0] and h[3][0] == h[4][0]: return True, [h[0][0], h[3][0]]
   elif h[0][0] == h[1][0] and h[2][0] == h[3][0] and h[3][0] == h[4][0]: return True, [h[2][0], h[0][0]]
   return False, []

def has_three(h):
   if   h[0][0] == h[1][0] and h[1][0] == h[2][0]: return True, [h[0][0], h[4][0], h[3][0]]
   elif h[1][0] == h[2][0] and h[2][0] == h[3][0]: return True, [h[1][0], h[4][0], h[0][0]]
   elif h[2][0] == h[3][0] and h[3][0] == h[4][0]: return True, [h[2][0], h[1][0], h[0][0]]
   return False, []

def has_two_pairs(h):
   if   h[0][0] == h[1][0] and h[2][0] == h[3][0]:
      if custom_sort(h[0], h[2]) > 0: return True, [h[0][0], h[2][0], h[4][0]]
      else:                           return True, [h[2][0], h[0][0], h[4][0]]
   elif h[0][0] == h[1][0] and h[3][0] == h[4][0]:
      if custom_sort(h[0], h[3]) > 0: return True, [h[0][0], h[3][0], h[2][0]]
      else:                           return True, [h[3][0], h[0][0], h[2][0]]
   elif h[1][0] == h[2][0] and h[3][0] == h[4][0]:
      if custom_sort(h[1], h[3]) > 0: return True, [h[1][0], h[3][0], h[0][0]]
      else:                           return True, [h[3][0], h[1][0], h[0][0]]
   return False, []

def has_pair(h):
   if   h[0][0] == h[1][0]: return True, [h[0][0], h[4][0], h[3][0], h[2][0]]
   elif h[1][0] == h[2][0]: return True, [h[1][0], h[4][0], h[3][0], h[0][0]]
   elif h[2][0] == h[3][0]: return True, [h[2][0], h[4][0], h[1][0], h[0][0]]
   elif h[3][0] == h[4][0]: return True, [h[3][0], h[2][0], h[1][0], h[0][0]]
   return False, []

def get_hand_value(h):
   o = order_hand(h)

   straight = flush = royal = False
   if is_straight(o): straight = True
   if is_flush(o):    flush    = True
   if is_royal(o):    royal    = True

   if straight and flush and royal: return 10 , o
   if straight and flush:           return  9 , o

   a, b = has_four(o)
   if a:                            return  8 , b
   a, b = is_full_house(o)
   if a:                            return  7 , b
   if flush:                        return  6 , o
   if straight:                     return  5 , o
   a, b = has_three(o)
   if a:                            return  4 , b
   a, b = has_two_pairs(o)
   if a:                            return  3 , b
   a, b = has_pair(o)
   if a:                            return  2 , b
   return 1, o[::-1]

def compare_hands(h1, h2):
   v1, t1 = get_hand_value(h1)
   v2, t2 = get_hand_value(h2)
   if v1 == v2:
      for i in range(len(t1)):
         if t1[i] > t2[i]: return True
         if t1[i] < t2[i]: return False
   return v1 > v2

s = 0
for i in a:
   h1, h2 = i[:5], i[5:]
   if compare_hands(h1, h2):
      s += 1

print s
