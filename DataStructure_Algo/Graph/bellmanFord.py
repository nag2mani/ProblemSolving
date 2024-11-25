class Edge:

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, src, dest, weight):
        self.edges.append(Edge(src, dest, weight))

    def bellman_ford(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for edge in self.edges:
                u, v, w = edge.src, edge.dest, edge.weight
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for edge in self.edges:
            u, v, w = edge.src, edge.dest, edge.weight
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(dist)


    def print_solution(self, dist):
        # print("Vertex Distance from Source:")
        for i in range(self.V):
            print(f"from vertex 0 to {i}\t distance {dist[i]}")


# Example usage:
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, -5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

g.bellman_ford(0)
