import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# Example usage
# Create a graph representing connections between locations and their distances
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4},
    'C': {'B': 1, 'D': 6},
    'D': {'E': 3},
    'E': {}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

# Print the shortest distances from the start node to all other nodes
for node, distance in distances.items():
    print(f"Shortest distance from {start_node} to {node}: {distance}")