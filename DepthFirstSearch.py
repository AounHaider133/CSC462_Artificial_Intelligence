def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = []

    path.append(start)
    visited.append(start)

    if start == goal:
        return path, visited

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result_path, result_visited = dfs(graph, neighbor, goal, path.copy(), visited.copy())
            # Check if result_path is not empty and the last node is the goal
            if result_path and result_path[-1] == goal:
                return result_path, result_visited

    return [], visited  # Return empty path and visited nodes if no path exists.

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start_node = 'A'
goal_node = 'F'
path, visited_nodes = dfs(graph, start_node, goal_node)
print("Path:", path)
print("Visited Nodes:", visited_nodes)
