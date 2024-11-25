import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i}\t{self.graph[i][parent[i]]}")

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.print_mst(parent)

# Example usage:
g = Graph(4)
# g.add_edge('A', 'B', 2)
# g.add_edge('B', 'A', 2)
# g.add_edge('B', 'C', 1)
# g.add_edge('C', 'B', 1)
# g.add_edge('C', 'D', 1)
# g.add_edge('D', 'C', 1)
# g.add_edge('D', 'A', 5)
# g.add_edge('A', 'D', 5)
# g.add_edge('B', 'D', 3)
# g.add_edge('D', 'B', 3)

g.add_edge(0, 1, 2)
g.add_edge(1, 0, 2)
g.add_edge(1, 2, 1)
g.add_edge(2, 1, 1)
g.add_edge(2, 3, 1)
g.add_edge(3, 2, 1)
g.add_edge(3, 0, 5)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 3)
g.add_edge(3, 1, 3)
g.prim_mst()

# print(sys.maxsize)
