import pprint
from collections import defaultdict 
class Graph: 

	def __init__(self,graph): 
		self.graph = graph
		self. ROW = len(graph) 

	def BFS(self,s, t, parent): 
		visited =[False]*(self.ROW) 
		queue=[] 
		queue.append(s) 
		visited[s] = True
		while queue: 
			u = queue.pop(0) 
			for ind, val in enumerate(self.graph[u]): 
				if visited[ind] == False and val > 0 : 
					queue.append(ind) 
					visited[ind] = True
					parent[ind] = u 
		return True if visited[t] else False
			

	def FordFulkerson(self, source, sink): 
		parent = [-1]*(self.ROW) 
		max_flow = 0
		while self.BFS(source, sink, parent) : 
			path_flow = float("Inf") 
			s = sink 
			while(s != source): 
				path_flow = min (path_flow, self.graph[parent[s]][s]) 
				s = parent[s] 
			max_flow += path_flow 
			v = sink 
			while(v != source): 
				u = parent[v] 
				self.graph[u][v] -= path_flow 
				self.graph[v][u] += path_flow 
				v = parent[v] 

		return max_flow 

inp = list(map(int, input().split()))
n = inp[0]
m = inp[1]
v = n + m + 2
c = inp [2]

graph = [[0 for k in range (v)] for j in range (v)]
# pprint.pprint(graph)

for i in range (1,m+1):
	graph[0][i] = 1


for i in range(1,m+1):
	inp = list(map(int, input().split()))
	num = inp[0]
	for j in range(1,num+1):
		graph[i][inp[j] + m + 1] = 1

for i in range(m+1,v-1):
	graph[i][v-1] = c

# pprint.pprint(graph)

g = Graph(graph) 
source = 0; sink = v-1

print (g.FordFulkerson(source, sink)) 

