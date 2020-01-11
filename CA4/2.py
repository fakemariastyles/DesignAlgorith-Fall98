import pprint
class GFG: 
    def __init__(self,graph): 
        self.graph = graph  
        self.ppl = len(graph) 
        self.jobs = len(graph[0]) 
    def bpm(self, u, matchR, seen): 
        for v in range(self.jobs): 
            if self.graph[u][v] and seen[v] == False: 
                seen[v] = True 
                if matchR[v] == -1 or self.bpm(matchR[v],  
                                               matchR, seen): 
                    matchR[v] = u 
                    return True
        return False
    def maxBPM(self): 
        matchR = [-1] * self.jobs 
        result = 0 
        for i in range(self.ppl): 
            seen = [False] * self.jobs 
            if self.bpm(i, matchR, seen): 
                result += 1
        return result 
  
bpGraph = [];

inp = list(map(int, input().split()))
m = inp[0]
n = inp [1]

for i in range(m):
  temp = []
  for j in range(n):
    if(j==i):
      temp.append(0)
    else:
      temp.append(1)
  bpGraph.append(temp)

b = int(input())


for i in range(b):
  inp = list(map(int, input().split()))
  x = inp[0]
  y = inp[1]
  bpGraph[x][y] = 0

# pprint.pprint(bpGraph)
  
g = GFG(bpGraph) 
  
print (g.maxBPM()) 