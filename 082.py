import urllib2
matrix = [ [ int(i) for i in line.split(',') ] for line in urllib2.urlopen('http://projecteuler.net/project/matrix.txt').read().strip().split('\r\n') ]
#matrix = [[ 131, 673, 234, 103, 18 ],
#          [ 201, 96,  342, 965, 150],
#          [ 630, 803, 746, 422, 111],
#          [ 537, 699, 497, 121, 956],
#          [ 805, 732, 524, 37,  331]]

class Graphe:

   class Node:
      def __init__(self, x, y):
         self.x = x
         self.y = y
         self.neighbors = []

   nodes = []

   def addNode(self, node):
      self.nodes.append(node)

   def addLink(self, node1, node2, value):
      for n in self.nodes:
         if node1[0] == n.x and node1[1] == n.y:
            n.neighbors.append((node2, value))
            return

   def getNode(self, node):
      for n in self.nodes:
         if n.x == node[0] and n.y == node[1]:
            return n

   def getNeighbors(node):
      pass


g = Graphe()


print 'Build graphe...'
for rowid, row in enumerate(matrix):
   for columnid, column in enumerate(row):
      n = Graphe.Node(rowid, columnid)
      g.addNode(n)

print 'Create links...'
for rowid, row in enumerate(matrix):
   for columnid, column in enumerate(row):
      # Right
      if columnid < len(row)-1:
         n1 = (rowid, columnid)
         n2 = (rowid, columnid+1)
         value = matrix[rowid][columnid+1]
         g.addLink(n1, n2, value)
      # Down
      if rowid < len(matrix)-1:
         n1 = (rowid, columnid)
         n2 = (rowid+1, columnid)
         value = matrix[rowid+1][columnid]
         g.addLink(n1, n2, value)
      # Up
      if rowid > 0:
         n1 = (rowid, columnid)
         n2 = (rowid-1, columnid)
         value = matrix[rowid-1][columnid]
         g.addLink(n1, n2, value)
print 'Links created...'


#for n in g.nodes:
#   print n.x, n.y, n.neighbors


def build_path(start, end, infos):
   path = []
   cost = 0
   smt = end
   if not infos[end]['pred']:
      return ([], -1)
   cost = infos[smt]['cost']
   fin = False
   while not fin:
      path.append(smt)
      smt = infos[smt]['pred']
      if smt == start:
         fin = True
   path.append(smt)
   path.reverse()
   return (path, cost)


def find(g, start, end):
   infos = {}
   queue = []
   path = []
   cost = 0
   for s in g.nodes:
      infos[(s.x, s.y)] = { 'cost': 99999999, 'visite': False, 'pred': None }
   infos[start]['cost'] = 0
   queue.append(start)
   infos[start]['visite'] = True
   fin = False
   while queue and not fin:
      min = queue[0]
      for n in queue:
         if infos[n]['cost'] < infos[min]['cost']:
            min = n
      queue.remove(min)
      smt = min
      for n in g.getNode(smt).neighbors:
         if not infos[n[0]]['visite']:
            queue.append(n[0])
            infos[n[0]]['visite'] = True

         if infos[n[0]]['pred'] != n[0]:
            if n[1] + infos[smt]['cost'] < infos[n[0]]['cost']:
               infos[n[0]]['cost'] = n[1] + infos[smt]['cost']
               infos[n[0]]['pred'] = smt

         if n[0][1] == len(matrix[0])-1:
            fin = True
            end = n[0]
   if fin:
      path, cost = build_path(start, end, infos)
   return (path, cost)


min = 9999999
for s in xrange(0, len(matrix)):
   start = (s, 0)
   end = (0, len(matrix[0])-1)
   path, cost = find(g, start, end)
   cost += matrix[start[0]][start[1]]
   if cost < min: min = cost
   print min, start, end
print min
