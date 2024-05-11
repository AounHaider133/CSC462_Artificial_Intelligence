import heapq

def ucs(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes.
    queue = [(0, start, [])]  # Priority queue for UCS with (cost, node, path).

    while queue:
        cost, node, path = heapq.heappop(queue)  # Get the node with the lowest cost.
        if node not in visited:
            visited.add(node)
            path = path + [node]

            if node == goal:
                return path, cost  # Return path and cost if goal is reached.

            for neighbor, neighbor_cost in graph.get(node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + neighbor_cost, neighbor, path))

    return "No path found.", 0  # Return this if no path exists.

# Example usage:
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 4, 'E': 2},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 1},
    'F': {}
}
start_node = 'A'
goal_node = 'F'
path, total_cost = ucs(graph, start_node, goal_node)
print("Path:", path)
print("Total Cost:", total_cost)
