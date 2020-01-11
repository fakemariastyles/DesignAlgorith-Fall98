
import sys
maxnum = 10000000000000
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  for row in range(vertices)] 

    def printMST(self, parent): 
        result = 0
        for i in range(1, self.V): 
            result += self.graph[i][parent[i]] 
        print(result)
  
    def minKey(self, key, mstSet): 
        min = sys.maxsize 
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
    def primMST(self): 
        key = [sys.maxsize] * self.V 
        parent = [None] * self.V
        key[0] = 0 
        mstSet = [False] * self.V 
  
        parent[0] = -1
  
        for cout in range(self.V): 
            u = self.minKey(key, mstSet) 
            mstSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
        self.printMST(parent)


n = int(input())
g = Graph(n+1)
arr = []
inp = []
for i in range(n+1):
    temp = []
    inp = list(map(int, input().split()))
    if(i == n):
        for j in range(len(inp)):
            arr[j].append(inp[j])
            temp.append(inp[j])
        temp.append(0)

    else:
        for j in range(len(inp)):
            temp.append(inp[j])

    arr.append(temp)

g.graph = arr
  
g.primMST(); 
  
