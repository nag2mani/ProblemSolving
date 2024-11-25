# Library for INT_MAX
import sys

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		print("Vertex 0 is S, 1 is A, 2 is B")
		for node in range(self.V):
			print("Distance from Source to", node, "is", dist[node])

	def minDistance(self, dist, sptSet):

		min = sys.maxsize

		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
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
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
					dist[v] = dist[u] + self.graph[u][v]
		self.printSolution(dist)

g = Graph(3)
g.graph = [
	[0,2,1],
	[float('inf'), 0, -2],
	[float('inf'), float('inf'), 0]
]

g.dijkstra(0)


