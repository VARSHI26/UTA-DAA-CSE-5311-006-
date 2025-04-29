def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    for _ in range(len(graph) - 1):
        for current_node, neighbors in graph.items():
            for neighbor, weight in neighbors.items():
                if distances[current_node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current_node] + weight
    for current_node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            if distances[current_node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")
    return distances
if __name__ == "__main__":
    graph = {
        "A": {"B": 3, "C": 7},
        "B": {"A": 8, "C": 2},
        "C": {"A": 5, "B": 1}
    }
    start_node = "A"
    shortest_distances = bellman_ford(graph, start_node)
    print(f"Shortest distances from node {start_node}:")
    for node, distance in shortest_distances.items():
        print(f"{node} : {distance}")
