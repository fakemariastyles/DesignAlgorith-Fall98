
import pprint  
import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 

    def minDistance(self, dist, sptSet): 
        min1 = sys.maxsize 
        min_index = 0

        for v in range(self.V): 
            if (dist[v] < min1) and (sptSet[v] == False): 
                min1 = dist[v] 
                min_index = v 
        return min_index 
    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 

            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V): 
                if (self.graph[u][v] > 0) and (sptSet[v] == False) and (dist[v] > dist[u] + self.graph[u][v]): 
                        dist[v] = dist[u] + self.graph[u][v] 
  
        print(dist[t])

v = 0
inp = list(map(int, input().split()))
n = inp[0]
s = inp [1]
t = inp[2]
inp = []
for i in range(n):
    temp = list(map(int, input().split()))
    inp.append(temp)
    for j in range(1,temp[0]+1):
        if (v < temp[j]):
            v = temp[j]


g = Graph(v+1) 
a = [[0 for i in range(v+1)] for j in range(v+1)]
for i in range(n):
    f = inp[i]
    temp = []
    for j in range(1,f[0]):
        x = f[j]
        y = f[j+1]
        if(x < y):
            a[x][y] = y - x
            a[y][x] = y - x
        else:
            a[x][y] = x - y
            a[y][x] = x - y

# pprint.pprint(a)
g.graph = a

g.dijkstra(s) 

