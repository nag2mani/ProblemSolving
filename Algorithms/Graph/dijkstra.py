import heapq

def dijkstra(graph, source):
    # Initialize distances to all vertices as infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0  # Distance from source to source is 0

    # Priority queue to store vertices with their current distances from the source
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Ignore this vertex if we have already found a shorter path to it
        if current_distance > distances[current_vertex]:
            continue

        # Update distances to adjacent vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # If this path is shorter than the current shortest path, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances



# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }

graph = {
    'S':{"A":2, "B":1},
    'A':{"B":-2},
    'B':{}
}
source = "S"
print(f"From {source} to ", dijkstra(graph, source))
