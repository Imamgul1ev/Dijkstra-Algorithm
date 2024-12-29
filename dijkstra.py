import heapq

def dijkstra(graph, source):

    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    priority_queue = [(0, source)]  # (distance, node)
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)


        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

# Example graph as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3, 'E': 5},
    'D': {'E': 1},
    'E': {}
}

source_node = 'A'
distances, previous_nodes = dijkstra(graph, source_node)

# Print the results
print(f"Shortest distances from {source_node}:")
for node, distance in distances.items():
    print(f"Node {node}: {distance}")

print("\nShortest path tree:")
for node, previous in previous_nodes.items():
    if previous is not None:
        print(f"{previous} -> {node}")
