import heapq

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    mst = []
    vertices = set(graph.keys())
    edges = [(weight, u, v) for u in graph for v, weight in graph[u]]
    heapq.heapify(edges)
    disjoint_set = DisjointSet(vertices)

    while edges:
        weight, u, v = heapq.heappop(edges)
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, weight))

    return mst

# Example usage:
graph = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 1), ('D', 3)],
    'C': [('B', 1), ('D', 1)],
    'D': [('A', 5), ('B', 3), ('C', 1)]
}

graph2 = {
    'A': [('B', 5), ('C', 3)],
    'B': [('E', 2), ('D', 6), ('C', 4), ('A', 5)],
    'C': [('A', 3), ('B', 4), ('D', 5), ('F', 6)],
    'D': [('B', 6), ('E', 6), ('F', 6), ('C', 5)],
    'E': [('B', 2), ('D', 6), ('F', 3), ('G', 4)],
    'F': [('C', 6), ('D', 6), ('E', 3), ('G', 4)],
    'G': [('E', 4), ('F', 4)],
}

minimum_spanning_tree = kruskal(graph2)
print("Minimum Spanning Tree (Kruskal's Algorithm):")
for edge in minimum_spanning_tree:
    print(edge)
